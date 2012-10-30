from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from cards.models import Card,CardEvent
from django.views.decorators.csrf import csrf_exempt

import binascii 
import base64

# Create your views here.

def is_card_valid(request, card_uid):
	print card_uid
	card = get_object_or_404(Card,tag_uid=card_uid)
	if (card.revoked == False and card.owner > 0):
		return render_to_response("cards/valid_card.txt",{'card':card})
	else:
		response = HttpResponse()
		response.status_code = 403 # TODO: raise an audit log
		return response

@csrf_exempt
def log_card_action(request, card_uid):
	event = CardEvent(tag_uid=card_uid)
	event.status=request.POST["status"]
	event.counter=request.POST["counter"]
	event.save()
	return render_to_response("cards/log_action_resp.txt")	

@csrf_exempt
def set_card_counter(request, card_uid):
	card = get_object_or_404(Card,tag_uid=card_uid)
	card.counter = request.POST["counter"]
	card.save()
	response = HttpResponse()
	response.status_code = 200
	return response

@csrf_exempt
def add_new_card(request, card_uid):
	card = Card(tag_uid=card_uid)
	encKeyA = request.POST["keyA"]
	encKeyB = request.POST["keyB"]

	card.keyA = encKeyA
	card.keyB = encKeyB	
	card.save()
	return render_to_response("cards/success.txt")

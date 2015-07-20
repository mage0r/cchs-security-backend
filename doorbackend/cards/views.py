from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from cards.models import Card,CardEvent
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime

import binascii 
import base64
import logging

logger = logging.getLogger('machine.events')

# Create your views here.

def is_card_valid(request, card_uid):
	print card_uid
	card = get_object_or_404(Card,tag_uid=card_uid)

	now_date = CardEvent.objects.filter(tag_uid=card_uid,time__gte=date.today()).order_by('-time')
	isIn = 0 
	if (len(now_date) >= 1 and now_date[0].status == 0):
		isIn = 1
	print now_date

	if ( card.user == None):
		username = "No.User"
		# This one will always exist
		card_revoked = str(card.revoked)
		user_is_active = "NA"
	else:
		username = card.user.username
		card_revoked = str(card.revoked)
		user_is_active = str(card.user.is_active)

	if (card.revoked == False and card.user.is_active ):
		event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	        event_text += " [Door.Back]"
        	event_text += " " + username
	        event_text += " (" + card.tag_uid + ")"
        	event_text += " Opened the Back Door"
		logger.info(event_text)

		return render_to_response("cards/valid_card.txt",{'card':card,'isIn':isIn})
	else:
		event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	        event_text += " [Door.Back]"
        	event_text += " " + username
	        event_text += " (" + card.tag_uid + ")"
        	event_text += " Door Access Denied!"
		event_text += " |Card Revoked=" + card_revoked
                event_text += " |User Active=" + user_is_active
		
		logger.info(event_text)

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

	# Log everything!
	event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	event_text += " [Door.Back]"
	event_text += " New Card"
	event_text += " (" + card_uid + ")"
	event_text += " Card Added"
	

	return render_to_response("cards/success.txt")

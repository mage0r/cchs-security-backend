from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from cards.models import Card,CardEvent
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def is_card_valid(request, card_uid):
	print card_uid
	card = get_object_or_404(Card,tag_uid=card_uid)
	return render_to_response("cards/valid_card.txt",{'card':card})


@csrf_exempt
def log_card_action(request, card_uid):
	event = CardEvent(tag_uid=card_uid)
	event.status=request.POST["status"]
	event.save()
	return render_to_response("cards/log_action_resp.txt")	


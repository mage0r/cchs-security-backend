from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from cards.models import Card
from machines.models import Machine,MachineAccess
from django.views.decorators.csrf import csrf_exempt
from datetime import date, datetime

import binascii 
import base64
import logging

logger = logging.getLogger('machine.events')

# Create your views here.

@csrf_exempt
def log_event(request):
	try:
		card = Card.objects.get(tag_uid=request.GET.get('card', False))
		username = card.user.username
		card_id = card.tag_uid
	except ObjectDoesNotExist:
		username = "Machine Operation"
		card_id = "NA"

	try:
		machine = Machine.objects.get(name=request.GET.get('machine', False))
		machine_name = machine.name
	except ObjectDoesNotExist:
		machine_name = "NA"

	event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	event_text += " [" + machine_name + "]"
	event_text += " " + username
	event_text += " (" + card_id + ")"
	event_text += " " + request.GET.get('text', False)
	
	logger.info(event_text)
	return render_to_response("cards/log_action_resp.txt")

@csrf_exempt
def is_card_valid(request, machine_name, card_uid):
	# well, no card and no machine would make this pointless...
	card = get_object_or_404(Card,tag_uid=card_uid)
	machine = get_object_or_404(Machine,name=machine_name)

	try:
		machine_access = MachineAccess.objects.get(user=card.user,machine=machine)
		machine_level = machine_access.level
		machine_level_display = machine_access.get_level_display()
	except ObjectDoesNotExist:
		machine_access = None
		machine_level = 0
		machine_level_display = "Not Cleared"

	if (card.revoked == False and card.user.is_active and int(machine_level) >= int(machine.minimum_level)):
		# log a successful response
		
		event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		event_text += " [" + machine.name + "]"
		event_text += " " + card.user.username
		event_text += " (" + card.tag_uid + ")"
		event_text += " Machine Unlocked!"
		event_text += " Card Revoked=" + str(card.revoked)
		event_text += "|User Active=" + str(card.user.is_active)
		event_text += "|User permission=" + str(machine_level)
		event_text += "|Machine requires=" + str(machine.minimum_level)

		logger.info(event_text)

		# return a "I'm happy" to the machine.
		return render_to_response("machines/valid_card.json",{'machine_name':machine.name,'card':card.tag_uid,'firstName':card.user.first_name,'lastName':card.user.last_name,'level':machine_level,'levelName':machine_level_display,})
	else:
		event_text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		event_text += " [" + machine.name + "]"
		event_text += " " + card.user.username
		event_text += " (" + card.tag_uid + ")"
		event_text += " Unlock denied!"
		event_text += " Card Revoked=" + str(card.revoked)
		event_text += "|User Active=" + str(card.user.is_active)
		event_text += "|User permission=" + str(machine_level)
		event_text += "|Machine requires=" + str(machine.minimum_level)

		logger.info(event_text)
		
		response = HttpResponse()
		response.status_code = 403 # TODO: raise an audit log
		return response	

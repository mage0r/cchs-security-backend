from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from datetime import date

import binascii 
import base64


# Create your views here.

def mass_user(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
        	if user.is_active:
			login(request, user)

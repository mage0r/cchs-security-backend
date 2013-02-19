
import os
import sys
#substitute doorbackend with the name of your project !!!
os.environ['DJANGO_SETTINGS_MODULE'] = 'doorbackend.settings'
# change this as appropriate
sys.path.append("/home/hacker/")
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

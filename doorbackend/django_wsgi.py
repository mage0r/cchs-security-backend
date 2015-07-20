
import os
import sys
#substitute doorbackend with the name of your project !!!
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# change this as appropriate
sys.path.append("/srv/django/dooraccess/doorbackend")
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

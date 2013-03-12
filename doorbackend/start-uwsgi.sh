#!/bin/sh
# Modify accordingly to your local environment
/Volumes/Data/Build/uwsgi-1.4.5/uwsgi  -s 127.0.0.1:18002 -pp .. -w django_wsgi_test -p 1 --env "DJANGO_SETTINGS_MODULE=doorbackend.settings"  --chdir `pwd`


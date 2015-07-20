#!/bin/sh
# Modify accordingly to your local environment
/usr/bin/uwsgi  -s 127.0.0.1:18002 -pp .. --wsgi-file django_wsgi_test -p 1 --env "DJANGO_SETTINGS_MODULE=settings"  --chdir `pwd`


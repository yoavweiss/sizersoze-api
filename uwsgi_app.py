#!/usr/bin/python
import sys
import os
import django.core.handlers.wsgi
sys.path.append("/opt/projects/sizersoze_api")
os.environ['DJANGO_SETTINGS_MODULE'] = "sizersoze_api.settings"
application = django.core.handlers.wsgi.WSGIHandler()



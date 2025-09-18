"""
WSGI config for dewya project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dewya.settings")

application = get_wsgi_application()

from django.core.management import call_command
from store.models import Product

try:
    if Product.objects.count() == 0:
        call_command('loaddata', 'products.json')
except Exception as e:
    print("Fixture load skipped:", e)

"""WSGI config for news_portal project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_portal.settings')

application = get_wsgi_application()

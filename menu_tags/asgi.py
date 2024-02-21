"""
ASGI config for menu_tags project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'menu_tags.settings')

application = get_asgi_application()

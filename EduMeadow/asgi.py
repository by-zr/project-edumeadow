# 180295818
"""
ASGI config for EduMeadow project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path
import MeadowChats.routing  
from MeadowChats.consumers import StudentChatConsumer  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EduMeadow.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Regular HTTP routing
    'websocket': AuthMiddlewareStack(
        URLRouter([
            MeadowChats.routing.websocket_urlpatterns 
        ])
    ),
})

# 180295818

from django.urls import path
from . import MeadowChats

websocket_urlpatterns = [
    path('chat/', MeadowChats.StudentChatConsumer.as_asgi()),
]
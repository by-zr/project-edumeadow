# 180295818

from django.urls import path
from . import views

urlpatterns = [
    # Trying to establish and test the connection of websocket to EduMeadow
    path('websocket-test/', views.websocket_connectiontest, name='websocket_test'), # http://127.0.0.1:8000/edumeadow/websocket-test/
    path('chat/', views.meadow_chat, name='chat'), # http://127.0.0.1:8000/edumeadow/chat/

]
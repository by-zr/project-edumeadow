# 180295818

from django.shortcuts import render

# Create your views here.
def websocket_connectiontest(request):
    return render(request, 'websocket_connection.html')

def meadow_chat(request):
    return render(request, 'meadow_chat.html')
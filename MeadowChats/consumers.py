# 180295818

from channels.generic.websocket import WebsocketConsumer
import json
from MeadowUsers.models import Student

# Tried to implement consumer for student chat function
class StudentChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        student_id = text_data_json['student_id']

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            # If student does not exist 
            return

        # Just trying to implement messaging logic first
        self.send(text_data=json.dumps({
            'message': message,
            'student_id': student_id,
            'student_name': student.name
        }))
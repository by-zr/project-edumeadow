# 180295818

from rest_framework import serializers
from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import Student

# Creating serializer for all platform users
class MeadowUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email']

# Creating serializer for Students
class StudentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ['id', 'user_id', 'gender', 'phone', 'date_of_birth']

# Creating serializer for Teachers
class MeadowUserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
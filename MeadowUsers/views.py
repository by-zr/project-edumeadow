# 180295818

import requests
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, action, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets
from .models import Student, Teacher
from .serializers import StudentSerializer

# Create your views here.

## API VIEW
@api_view(['POST'])
def student_list(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def student_detail(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
@api_view(['GET', 'PUT'])
@action(detail=False)
@permission_classes([IsAuthenticated]) 
def me(request):
    student = get_object_or_404(Student, pk=request.user.id)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def user_register(request):
    if request.method == 'POST':
        url = 'http://localhost:8000/auth/users/'
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password')
        }
        response = requests.post(url, data=data)
        if response.status_code == 201:
            # Redirect to login page 
            return render(request, 'login.html')
        else:
            # To display error message
            error_message = response.json().get('detail', 'Unknown error')
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

# For platform users to log in EduMeadow
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'student'):
                student = Student.objects.get(user=user)
                return redirect('/edumeadow')  
            elif hasattr(user, 'teacher'):
                teacher = Teacher.objects.get(user=user)
                return redirect('/edumeadow')  
            else:
                return redirect('/edumeadow') 
        else:
            # If authentication fails, display error message
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    # Render the login page if authentication fails
    return render(request, 'login.html')

# To enable user log out
def user_logout(request):
    logout(request)
    return redirect('/')
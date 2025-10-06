# 180295818

from django.db import models
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Creating model for User as Abstract User
class User(AbstractUser):
    email = models.EmailField(unique=True)

# Creating model for Students
class Student(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    
    # first_name = models.CharField(max_length=255, default='')
    # last_name = models.CharField(max_length=255, default='')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')
    # email = models.EmailField(unique=True, default='')
    phone = models.CharField(max_length=255, default='')
    date_of_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'
        # return self.first_name + ' ' + self.last_name
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name
    
    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name
    
    class Meta:
        ordering = ['user__first_name', 'user__last_name']

# Creating model for Teachers
class Teacher(models.Model):
    PREFIX_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Miss.', 'Miss.'),
        ('Ms.', 'Ms.'),
        ('Mrs.', 'Mrs.'),
        ('Mdm.', 'Mdm.'),
        ('Dr.', 'Dr.'),
        ('Prof.', 'Prof.'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    # IMO should change to the custom user model, user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) for easier customization
    prefix = models.CharField(max_length=10, choices=PREFIX_CHOICES, default='')
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True, default='')
    phone = models.CharField(max_length=255, default='')
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.prefix + ' ' + self.first_name + ' ' + self.last_name

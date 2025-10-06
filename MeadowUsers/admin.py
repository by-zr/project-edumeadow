# 180295818

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from . import models

# Register your models here.

# Registering Admin in Admin page
@admin.register(User)
class MeadowAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
        }),
    )

# Registering Student model in Admin page
@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 8
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']

# Registering Teacher model in Admin page
@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_per_page = 8
    ordering = ['first_name', 'last_name']
    search_fields = ['first_name__istartswith', 'last_name__istartswith']
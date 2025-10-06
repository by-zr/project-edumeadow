# 180295818

from django import forms
from django.contrib import admin
from django.db.models import Count 
from django.urls import reverse
from django.utils.html import format_html
from . import models

# Register your models here.

# To register Course model in Admin 
@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'teacher', 'total_students', 'total_lessons']
    list_editable = ['teacher']
    list_per_page = 8
    ordering = ['title']
    search_fields = ['title__istartswith', 'teacher__first_name__istartswith', 'teacher__last_name__istartswith']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            total_students=Count('enrolment__student', distinct=True),
            total_lessons=Count('lesson', distinct=True)
        )
        return queryset
    
    def total_students(self, obj):
        return obj.total_students
    
    def total_lessons(self, obj):
        return obj.total_lessons

# To register Lesson model in Admin 
@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    list_per_page = 8
    ordering = ['course']

# To register Enrolment model in Admin 
@admin.register(models.Enrolment)
class EnrolmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrolled_on']
    search_fields = ['student__first_name__istartswith', 'student__last_name__istartswith']

# To register FeaturedCourse model in Admin 
@admin.register(models.FeaturedCourse)
class FeaturedCourse(admin.ModelAdmin):
    list_display = ['title']
    list_per_page = 8    

# To register Post model in Admin 
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_on', 'author_teacher', 'author_student', 'user')
    search_fields = ('title',)
    list_filter = ('posted_on',)
    empty_value_display = ''

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].required = False
        form.base_fields['author_teacher'].required = False
        form.base_fields['author_student'].required = False
        form.base_fields['user'].required = False
        return form

# To register Comment model in Admin 
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'commented_on', 'author_teacher', 'author_student', 'user')
    search_fields = ('user__username', 'post__title')
    list_filter = ('commented_on',)
    empty_value_display = ''

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['author_teacher'].required = False
        form.base_fields['author_student'].required = False
        form.base_fields['user'].required = False
        return form

# To register Feedback model in Admin 
@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['course', 'author_student', 'title', 'created_on']
    list_filter = ['course', 'author_student', 'created_on']
    search_fields = ['title', 'content']
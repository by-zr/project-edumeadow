# 180295818

import random
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from MeadowUsers.models import Student, Teacher

# Create your models here.

# Creating model for Featured Courses
class FeaturedCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title

# Creating model for Courses
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    featured_course = models.ManyToManyField(FeaturedCourse)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

# Creating model to contain Course Images
class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='')

# Creating model for Student Enrolments
class Enrolment(models.Model):
    ENROLMENT_STATUS_PENDING = 'P'
    ENROLMENT_STATUS_ENROLLED = 'E'
    ENROLMENT_STATUS_CANCELLED = 'C'
    ENROLMENT_STATUS_CHOICES = [
        (ENROLMENT_STATUS_PENDING, 'Pending'),
        (ENROLMENT_STATUS_ENROLLED, 'Enrolled'),
        (ENROLMENT_STATUS_CANCELLED, 'Cancelled')
    ]

    enrolled_on = models.DateTimeField(auto_now_add=True)
    enrolment_status = models.CharField(
        max_length=1, choices=ENROLMENT_STATUS_CHOICES, default=ENROLMENT_STATUS_PENDING)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

# Creating model for Lessons for each Course
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']

# Creating model for Posts
class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(blank=True)
    author_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    author_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def author_name(self):
        if self.author_teacher:
            return self.author_teacher.prefix + ' ' + self.author_teacher.first_name + ' ' + self.author_teacher.last_name
        elif self.author_student:
            return self.author_student.user.first_name + ' ' + self.author_student.user.last_name
        elif self.user:
            if self.user.is_superuser:
                return "Superuser"
            else:
                return self.user.username
        else:
            return "Admin"

# Creating model for Comments
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    author_student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    commented_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def author_name(self):
        if self.author_teacher:
            return self.author_teacher.prefix + ' ' + self.author_teacher.first_name + ' ' + self.author_teacher.last_name
        elif self.author_student:
            return self.author_student.user.first_name + ' ' + self.author_student.user.last_name
        elif self.user:
            if self.user.is_superuser:
                return "Admin"
            else:
                return self.user.username
        else:
            random_id = random.randint(1000, 9999) # To Assign random integer behind MeadowUser for each interaction
            return f"MeadowUser{random_id}"

# Creating model for Student's Feedbacks
class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    author_student = models.ForeignKey(Student, on_delete=models.CASCADE)
    title = models.CharField(max_length=255,)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def author_name(self):
        return self.author_student.user.first_name + ' ' + self.author_student.user.last_name



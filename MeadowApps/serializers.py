# 180295818

from rest_framework import serializers
from .models import Course, Lesson, Enrolment, CourseImage
from MeadowUsers.models import Student

# Creating serializer for Course model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'teacher']

# Creating serializer for Course image model
class CourseImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseImage
        fields = ['id', 'image']

# Creating serializer for Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'course']
    
# Creating serializer for Enrolment 
class EnrolmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseImage.objects.create(course_id=course_id, **validated_data)
    
    class Meta:
        model = Enrolment
        fields = ['id', 'student', 'enrolled_on', 'enrolment_status']


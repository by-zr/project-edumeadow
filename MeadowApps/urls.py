# 180295818

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

# Router Configuration
router = DefaultRouter()

# URL Configuration
urlpatterns = [
    path('', views.home, name='home'), # Default starting page http://127.0.0.1:8000/

    # API Views
    path('course/', views.course_list), # APIview for Course list http://127.0.0.1:8000/course/
    path('course/<int:id>/', views.course_detail), # APIview for individual Course detail http://127.0.0.1:8000/course/<int:id>
    path('lesson/', views.lesson_list), # APIview for Lesson list http://127.0.0.1:8000/lesson/
    path('lesson/<int:id>/', views.lesson_detail), # APIview for individual Lesson detail http://127.0.0.1:8000/lesson/<int:id>
    path('enrolment/', views.enrolment_list), # Enrolment APIview http://127.0.0.1:8000/edumeadow/enrolment/

    # After Log in
    path('edumeadow/', views.dashboard, name='dashboard'), # Dashboard after logging in http://127.0.0.1:8000/edumeadow/
    # Continue Learning
    path('mycourses/', views.my_courses, name='my_courses'), # http://127.0.0.1:8000/edumeadow/mycourses/
    path('mycourses/student/', views.student_mycourses, name='student_mycourses'), # For Student
    path('mycourses/teacher/', views.teacher_mycourses, name='teacher_mycourses'), # For Teacher
    path('browse', views.browse_courses, name='browse'), # Page to browse all courses http://127.0.0.1:8000/edumeadow/browse
    path('feedbacks/', views.reviews, name='reviews'), # Page to view all student's feedback http://127.0.0.1:8000/edumeadow/feedbacks/
    path('feedbackform/', views.feedback_form, name='feedback_form'), # Page for student to submit feedback http://127.0.0.1:8000/edumeadow/feedbackform/
    path('profile/', views.profile, name='profile'), # Profile page http://127.0.0.1:8000/edumeadow/profile/
    path('editprofile/', views.profile_edit, name='edit_profile'), # Page to edit profile http://127.0.0.1:8000/edumeadow/editprofile/

    # Before Log in
    path('about/', views.about, name='about'), # About EduMeadow page http://127.0.0.1:8000/edumeadow/about/
    path('courses/', views.courses, name='courses'), # Page to view platform courses http://127.0.0.1:8000/edumeadow/courses/
    path('reviews/', views.home_reviews, name='home_reviews'), # Page to view platform reviews http://127.0.0.1:8000/edumeadow/reviews/

] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
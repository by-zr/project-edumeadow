# 180295818

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from . import views
from .views import user_register, user_login, user_logout

# Router Configuration
# router = routers.DefaultRouter()
# router.register('students', views.StudentViewSet)

# URL Configuration
urlpatterns = [
    # API VIEW
    path('student/', views.student_list), # For the list of students http://127.0.0.1:8000/edumeadow/student/
    path('student/<int:id>/', views.student_detail), # For individual student http://127.0.0.1:8000/edumeadow/student/<int:id>
    path('student/me/', views.me), # For user who is student to get their api view http://127.0.0.1:8000/edumeadow/student/me

    # REGISTRATION
    path('register/', user_register, name='user_register'), # Register form http://127.0.0.1:8000/edumeadow/register/
    path('login/', user_login, name='user_login'), # Log in form http://127.0.0.1:8000/edumeadow/login/
    path('logout/', user_logout, name='user_logout'), # Route account to log out http://127.0.0.1:8000/edumeadow/logout

    # JWT AUTH URLS
    # http://127.0.0.1:8000/auth/jwt/create
    # http://127.0.0.1:8000/auth/
    # http://127.0.0.1:8000/auth/users
    # http://127.0.0.1:8000/auth/users/me/
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


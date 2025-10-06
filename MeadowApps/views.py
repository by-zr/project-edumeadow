# 180295818

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course, Lesson, Enrolment, CourseImage, Post, Comment, Student, Feedback
from .serializers import CourseSerializer, LessonSerializer, EnrolmentSerializer, CourseImageSerializer
from .forms import PostForm, CommentForm, FeedbackForm, TeacherForm, StudentForm

# Create your views here.

# View for starting/ index page
def home(request):
    return render(request, 'index.html')

# View for Courses page to display all platform courses
def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

# View for platform users to browse all courses
@login_required
def browse_courses(request):
    courses = Course.objects.all()

    if request.method == 'POST':
        course_id = request.POST.get('course_id')
        if course_id:
            course = Course.objects.get(pk=course_id)
            student = Student.objects.get(user=request.user)
            if not is_enrolled(course, request.user):
                enrolment = Enrolment(course=course, student=student)
                enrolment.save()
            return redirect('/mycourses')
        
    return render(request, 'browse.html', {'courses': courses})

def is_enrolled(course, user):
    student = Student.objects.get(user=user)
    return Enrolment.objects.filter(course=course, student=student).exists()

# View to display all platform reviews
def home_reviews(request):
    reviews = Feedback.objects.all()
    return render(request, 'home_reviews.html', {'reviews': reviews})

# View to render feedback form for students to submit their feedback
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = request.user
            if hasattr(user, 'student'):
                feedback = form.save(commit=False)
                feedback.author_student_id = request.user.student.id  
                feedback.save()
                return redirect('/edumeadow/feedbacks')  # Redirect to a success page
        else:
                messages.error(request, "Only students are allowed to submit feedback.")
                return render(request, 'feedback.html', {'form': form})
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

# View to display courses that student enrolled, or courses that teacher in-charge of
@login_required
def my_courses(request):
    if hasattr(request.user, 'teacher'):
        return redirect('teacher_mycourses')  # Redirect to teacher my courses page
    elif hasattr(request.user, 'student'):
        return redirect('student_mycourses')  # Redirect to student my courses page
    else:
        return render(request, 'my_courses.html')  # For users that are not student or teacher

@login_required
def student_mycourses(request):
    student_profile = Student.objects.get(user=request.user) # To get the courses associated with the student profile
    enrolments = Enrolment.objects.filter(student=student_profile)
    student_mycourses = [enrolment.course for enrolment in enrolments]

    return render(request, 'student_mycourses.html', {'student_mycourses': student_mycourses})

@login_required
def teacher_mycourses(request):
    return render(request, 'teacher_mycourses.html')

# View to render About page 
def about(request):
    return render(request, 'about.html')

# To display all reviews sort by creation date
def reviews(request):
    reviews = Feedback.objects.order_by('-created_on')
    return render(request, 'reviews.html', {'reviews': reviews})

# Dashboard after user log in to platform
@login_required
def dashboard(request):
    user = request.user
    if hasattr(user, 'teacher'):
        profile = user.teacher
    elif hasattr(user, 'student'):
        profile = user.student
    else:
        profile = None

    # Implementing form to enable Post function
    if request.method == 'POST':
        pform = PostForm(request.POST)
        if pform.is_valid():
            post = pform.save(commit=False)
            
            if hasattr(request.user, 'teacher'):
                post.author_teacher = request.user.teacher
            elif hasattr(request.user, 'student'):
                post.author_student = request.user.student
            post.save()
            return redirect('/edumeadow')  # Redirect back to dashboard
    else:
        pform = PostForm()

    # Implementing form to enable Comment function
    if request.method == 'POST':
        cform = CommentForm(request.POST)
        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.content = request.POST.get('comment')  
            comment.post_id = request.POST.get('post_id') 

            if hasattr(request.user, 'teacher'):
                comment.author_teacher = request.user.teacher
            elif hasattr(request.user, 'student'):
                comment.author_student = request.user.student
            comment.save()
            return redirect('/edumeadow')  # Redirect back to dashboard
    else:
        cform = CommentForm()

    # Both posts and comments are sorted by creation date in a descending order
    posts = Post.objects.order_by('-posted_on')
    comments = Comment.objects.order_by('-commented_on')

    return render(request, 'dashboard.html', {'user': user, 'profile': profile, 'posts': posts, 'comments': comments, 'pform': pform, 'cform': cform})

# Wanted to route user to their respective profiles
@login_required
def profile(request):
    user = request.user
    if hasattr(user, 'teacher'):
        profile = user.teacher
        profile_type = 'teacher'
    elif hasattr(user, 'student'):
        profile = user.student
        profile_type = 'student'
    else:
        profile = None
        profile_type = None
    
    return render(request, 'profile.html', {'user': user, 'profile': profile, })

# For students to edit their profile information
@login_required
def profile_edit(request):
    user = request.user
    if hasattr(user, 'student'):
        profile = user.student
    else:
        profile = None
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful update
    else:
        form = StudentForm(instance=profile)
    
    return render(request, 'edit_profile.html', {'user': user, 'profile': profile, 'form': form})

## API VIEWS 

# API view for list of Courses
@api_view(['GET', 'POST'])
def course_list(request):
    if request.method == 'GET':
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# To view individual Course detail by <int:id> 
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, id):
    course = Course.objects.get(pk=id)
    if request.method == 'GET':
        try:
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'PUT':
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if course.enrolment_set.count() > 0:
            return Response({'error': 'Unable to delete. There are still students enrolled in this course.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

## Wanted to implement APIview for Course images
#   @api_view(['GET', 'POST'])
#   def course_image(request, course_pk):
#   queryset = CourseImage.objects.filter(course_id=course_pk)
#   serializer = CourseImageSerializer(queryset, many=True)
#   return Response(serializer.data)

# To get the list of lessons for each course identified by course id
@api_view(['GET', 'POST'])
def lesson_list(request):
    if request.method == 'GET':
        queryset = Lesson.objects.all()
        serializer = LessonSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LessonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
       
# Individual lesson view access by <int:id> 
@api_view(['GET', 'PUT', 'DELETE'])
def lesson_detail(request, id):
    lesson = get_object_or_404(Lesson, pk=id)
    if request.method == 'GET':
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LessonSerializer(lesson, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# To get the list of enrolments
@api_view(['GET', 'POST'])
def enrolment_list(request):
    if request.method == 'GET':
        queryset = Enrolment.objects.all()
        serializer = EnrolmentSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EnrolmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)



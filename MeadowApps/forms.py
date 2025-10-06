# 180295818

from django import forms
from .models import Post, Comment, Feedback
from MeadowUsers.models import Student, Teacher

# Creating form for Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': "What's on your mind?"})
        }

# Creating form for Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Creating form for Student's Feedbacks
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.Textarea(attrs={'placeholder': "How do you feel about this course?"})
        }

# Creating form for Teachers to edit Profile Biography
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['bio']

# Creating form for Students to edit Profile Biography
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['date_of_birth', 'bio']
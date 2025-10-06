# EduMeadow - Online Learning Platform

EduMeadow is a comprehensive Django-based online learning platform that provides a modern educational experience for students and teachers. The platform features course management, real-time chat functionality, user authentication, and a RESTful API.

## 🎯 Project Overview

EduMeadow is designed to facilitate online education with features including:
- **Course Management**: Create, browse, and enroll in courses
- **User Authentication**: Secure login/registration system with JWT tokens
- **Real-time Communication**: WebSocket-based chat functionality
- **Social Features**: Posts, comments, and feedback system
- **RESTful API**: Complete API for course and user management
- **Role-based Access**: Separate interfaces for students and teachers

## 🏗️ Architecture

The project follows Django's app-based architecture with three main applications:

### Core Applications
- **MeadowApps**: Main application handling courses, lessons, posts, comments, and feedback
- **MeadowUsers**: User management with custom user model, students, and teachers
- **MeadowChats**: Real-time chat functionality using Django Channels and WebSockets

## 🛠️ Technology Stack

### Backend
- **Django 5.0.2**: Web framework
- **Django REST Framework**: API development
- **Django Channels**: WebSocket support for real-time features
- **Djoser**: Authentication and user management
- **JWT**: JSON Web Token authentication
- **SQLite**: Database (development)
- **Redis**: Caching and session storage
- **Pillow**: Image processing

### Frontend
- **Bootstrap 5.3.3**: UI framework
- **JavaScript**: Client-side functionality
- **WebSocket**: Real-time communication

### Development Tools
- **Django Extensions**: Development utilities
- **Graphviz**: Database visualization
- **Pytest**: Testing framework

## 📋 Features

### For Students
- User registration and authentication
- Browse and enroll in courses
- View enrolled courses
- Submit feedback and reviews
- Create posts and comments
- Real-time chat functionality
- Profile management

### For Teachers
- Course creation and management
- Student enrollment tracking
- Post creation and interaction
- Profile management with professional information

### General Features
- Responsive web design
- RESTful API endpoints
- JWT-based authentication
- Real-time WebSocket communication
- Image upload support
- Admin panel for content management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11
- Node.js (for frontend dependencies)
- Redis server

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd awd_cw2
   ```

2. **Set up Python environment**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

3. **Install frontend dependencies**
   ```bash
   npm install
   ```

4. **Set up Redis** (for WebSocket support)
   ```bash
   # On Windows, use the included Redis or install separately
   # Start Redis server
   redis-server
   ```

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/
   - API documentation: http://127.0.0.1:8000/auth/

## 📁 Project Structure

```
awd_cw2/
├── EduMeadow/                 # Main Django project
│   ├── settings.py           # Project settings
│   ├── urls.py              # Main URL configuration
│   └── asgi.py              # ASGI configuration for WebSockets
├── MeadowApps/              # Main application
│   ├── models.py            # Course, Lesson, Post, Comment models
│   ├── views.py             # View functions and API endpoints
│   ├── urls.py              # URL patterns
│   ├── forms.py             # Django forms
│   ├── serializers.py       # DRF serializers
│   └── templates/           # HTML templates
├── MeadowUsers/             # User management app
│   ├── models.py            # User, Student, Teacher models
│   ├── views.py             # Authentication views
│   ├── urls.py              # User-related URLs
│   └── serializers.py       # User serializers
├── MeadowChats/             # Chat functionality
│   ├── consumers.py         # WebSocket consumers
│   ├── routing.py           # WebSocket routing
│   └── templates/           # Chat templates
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User-uploaded files
├── tests/                   # Test files
├── Pipfile                  # Python dependencies
├── package.json             # Node.js dependencies
└── manage.py               # Django management script
```

## 🔌 API Endpoints

### Authentication
- `POST /auth/users/` - User registration
- `POST /auth/jwt/create/` - JWT token creation
- `GET /auth/users/me/` - Current user info

### Courses
- `GET /course/` - List all courses
- `POST /course/` - Create new course
- `GET /course/<id>/` - Get course details
- `PUT /course/<id>/` - Update course
- `DELETE /course/<id>/` - Delete course

### Lessons
- `GET /lesson/` - List all lessons
- `POST /lesson/` - Create new lesson
- `GET /lesson/<id>/` - Get lesson details
- `PUT /lesson/<id>/` - Update lesson
- `DELETE /lesson/<id>/` - Delete lesson

### Students
- `POST /student/` - Create student profile
- `GET /student/<id>/` - Get student details
- `PUT /student/<id>/` - Update student profile
- `GET /student/me/` - Current student profile

### Enrollments
- `GET /enrolment/` - List all enrollments
- `POST /enrolment/` - Create new enrollment

## 🌐 Web Pages

### Public Pages
- `/` - Home page
- `/about/` - About EduMeadow
- `/courses/` - Browse all courses
- `/reviews/` - View platform reviews

### Authentication
- `/register/` - User registration
- `/login/` - User login
- `/logout/` - User logout

### Authenticated Pages
- `/edumeadow/` - Dashboard
- `/browse` - Browse and enroll in courses
- `/mycourses/` - My enrolled courses
- `/profile/` - User profile
- `/editprofile/` - Edit profile
- `/feedbackform/` - Submit feedback
- `/feedbacks/` - View all feedback
- `/chat/` - Real-time chat
- `/websocket-test/` - WebSocket connection test

## 🗄️ Database Models

### Core Models
- **User**: Custom user model extending AbstractUser
- **Student**: Student profile with personal information
- **Teacher**: Teacher profile with professional details
- **Course**: Course information and metadata
- **Lesson**: Individual lessons within courses
- **Enrolment**: Student-course enrollment tracking
- **Post**: Social posts by users
- **Comment**: Comments on posts
- **Feedback**: Student feedback and reviews
- **CourseImage**: Course image attachments

## 🔧 Configuration

### Environment Variables
The application uses Django's default settings. For production deployment, consider setting:
- `DEBUG = False`
- `SECRET_KEY` (use a secure key)
- `ALLOWED_HOSTS` (specify your domain)
- Database configuration (PostgreSQL recommended for production)

### WebSocket Configuration
WebSocket functionality is configured in `EduMeadow/asgi.py` and uses Redis as the channel layer backend.

## 🧪 Testing

Run tests using pytest:
```bash
pytest
```

Or using Django's test runner:
```bash
python manage.py test
```

## 🚀 Deployment

### Production Checklist
1. Set `DEBUG = False` in settings
2. Configure a production database (PostgreSQL recommended)
3. Set up Redis for production
4. Configure static file serving
5. Set up SSL/HTTPS
6. Configure proper logging
7. Set up monitoring and error tracking

### Docker Deployment (Optional)
The project can be containerized using Docker with separate containers for:
- Django application
- Redis server
- Database (PostgreSQL)
- Nginx (reverse proxy)

## 🎓 Learning Project

This EduMeadow platform is developed as a **learning project** for educational purposes, specifically as part of the University of London AWD (Advanced Web Development) coursework. The project serves as a comprehensive demonstration of modern web development practices and technologies.

### Learning Objectives Achieved
- **Django Framework**: Full-stack web application development
- **RESTful API Design**: Creating and consuming REST APIs with Django REST Framework
- **Real-time Communication**: Implementing WebSocket functionality with Django Channels
- **Authentication & Authorization**: JWT-based authentication system
- **Database Design**: Complex relational database models and relationships
- **Frontend Integration**: Bootstrap-based responsive UI design
- **Project Architecture**: Modular Django app structure and best practices

## 🚀 Future Possible Implementations

While this is primarily a learning project, the EduMeadow platform has potential for future enhancements and real-world applications:

### Enhanced Features
- **Video Streaming**: Integration with video platforms for course content delivery
- **Live Classes**: Real-time video conferencing for interactive learning sessions
- **Mobile App**: Native iOS/Android applications for mobile learning
- **Advanced Analytics**: Learning progress tracking and performance analytics
- **Payment Integration**: Course payment processing and subscription management
- **Multi-language Support**: Internationalization for global accessibility
- **Advanced Search**: Elasticsearch integration for better content discovery
- **File Management**: Cloud storage integration for course materials
- **Notification System**: Email and push notifications for course updates
- **Discussion Forums**: Advanced forum system for course discussions

### Technical Improvements
- **Microservices Architecture**: Breaking down into smaller, scalable services
- **Container Orchestration**: Kubernetes deployment for production scaling
- **CI/CD Pipeline**: Automated testing and deployment workflows
- **Performance Optimization**: Caching strategies and database optimization
- **Security Enhancements**: Advanced security measures and vulnerability testing
- **API Versioning**: Proper API versioning for backward compatibility
- **Monitoring & Logging**: Comprehensive application monitoring and logging
- **Load Balancing**: High availability and traffic distribution

### Educational Technology Integration
- **Learning Management System (LMS)**: Full-featured LMS capabilities
- **Assessment Tools**: Quizzes, assignments, and automated grading
- **Progress Tracking**: Detailed learning analytics and progress reports
- **Certification System**: Digital certificates and credential management
- **Collaborative Learning**: Group projects and peer-to-peer learning features
- **Adaptive Learning**: AI-powered personalized learning paths

---

**Note**: This is an educational project developed for coursework purposes. The application demonstrates modern web development practices using Django, REST APIs, and real-time communication features. While designed for learning, it showcases the potential for building comprehensive educational technology platforms.

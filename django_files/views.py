from django.shortcuts import render
from .models import Course, UserPerformance
from django.contrib.auth.decorators import login_required

# Example of a Django view. Each view will render a corresponding template.

def login_page(request):
    """
    Renders the login and signup page.
    """
    return render(request, 'login_signup.html')

def browse_courses(request):
    """
    Renders the browse courses page.
    """
    courses = Course.objects.all()
    return render(request, 'browse_courses.html', {'courses': courses})

@login_required
def user_dashboard(request):
    """
    Renders the user dashboard with dynamic data.
    """
    user_courses = UserPerformance.objects.filter(user=request.user)
    
    # Mock data for demonstration purposes
    enrolled_count = user_courses.count()
    completed_count = user_courses.filter(progress_percentage=100).count()
    
    if enrolled_count > 0:
        avg_score = sum([p.score for p in user_courses]) / enrolled_count
    else:
        avg_score = 0
        
    context = {
        'user_name': request.user.username,
        'enrolled_count': enrolled_count,
        'completed_count': completed_count,
        'avg_score': int(avg_score),
        'user_courses': user_courses,
    }
    return render(request, 'user_dashboard.html', context)

def ranking_page(request):
    """
    Renders the user ranking page.
    """
    rankings = UserPerformance.objects.order_by('-score')[:10]
    return render(request, 'ranking.html', {'rankings': rankings})

def course_page(request, course_id):
    """
    Renders a specific course page.
    """
    course = Course.objects.get(pk=course_id)
    return render(request, 'course_page.html', {'course': course})


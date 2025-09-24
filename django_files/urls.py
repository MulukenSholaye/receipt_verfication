from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('browse/', views.browse_courses, name='browse'),
    path('ranking/', views.ranking_page, name='ranking'),
    path('course/<int:course_id>/', views.course_page, name='course_page'),
]

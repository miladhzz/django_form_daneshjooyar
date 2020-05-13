from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'creator'

urlpatterns = [
    path('', views.CreateResume.as_view(), name='create_resume'),
    path('<int:resume_id>/', views.edit_resume, name='edit_resume'),
    path('educations/<int:resume_id>/', views.create_resume_education, name='create_resume_educations'),
    path('skills/<int:resume_id>/', views.create_resume_skill, name='create_resume_skills'),
    path('experiences/<int:resume_id>/', views.create_resume_experience, name='create_resume_experiences'),

    path('registration/login/', auth_views.LoginView.as_view(), name='login'),
    path('registration/logout/', views.logout_view, name='logout'),
    path('registration/register/', views.register_view, name='register'),
    path('registration/profile/', views.view_profile, name='profile'),
    path('registration/edit-profile/', views.edit_profile, name='edit_profile'),
    path('registration/password/', views.change_password, name='change_password'),
]

from django.urls import path
from . import views

app_name = 'creator'

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('educations/', views.create_resume_education, name='create_resume_educations'),
    path('skills/', views.create_resume_skill, name='create_resume_skills'),
    path('experiences/', views.create_resume_experience, name='create_resume_experiences'),
]

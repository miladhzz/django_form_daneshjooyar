from django.urls import path
from . import views

app_name = 'creator'

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
    path('<int:resume_id>/', views.edit_resume, name='edit_resume'),
    path('educations/<int:resume_id>/', views.create_resume_education, name='create_resume_educations'),
    path('skills/<int:resume_id>/', views.create_resume_skill, name='create_resume_skills'),
    path('experiences/<int:resume_id>/', views.create_resume_experience, name='create_resume_experiences'),
]

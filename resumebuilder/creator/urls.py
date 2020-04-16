from django.urls import path
from . import views

app_name = 'creator'

urlpatterns = [
    path('', views.create_resume, name='create_resume'),
]

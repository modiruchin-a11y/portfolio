from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project/',views.project,name='project'),
    path('project_d/<int:id>/', views.project_d, name='project_d'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('add/', views.AddStudent, name='AddStudent'),
    path('delete/<int:s_id>', views.RemoveStudent, name='RemovStudent'),
    path('edit/<int:s_id>', views.EditStudent, name='EditStudent'),
    path('add_file/', views.AddFromFile, name='AddFromFile'),
]

from django.contrib import admin
from django.urls import path, include
from easy import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bussiness', views.bussiness, name='bussiness'),
    path('Contact', views.contact, name="Contact"),
    path('news', views.news, name="news"),
    path('Entertainment', views.Entertainment, name="Entertainment"),
    path('sports', views.sports, name="sports"),
    path('health', views.health, name="health"),
    path('science', views.science, name="science"),
]
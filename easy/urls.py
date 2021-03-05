from django.contrib import admin
from django.urls import path, include
from easy import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bussiness', views.bussiness, name='bussiness'),
    path('sinup', views.sinup, name='sinup'),
    path('login', views.loginhandle, name='login'),
    path('logout',views.logouthandle,name = 'logout'),
    path('Contact', views.contact, name="Contact"),
    path('news', views.news, name="news")
#    path('', views.View_css, name="view_css")

]
from django.urls import path
from django.contrib import admin
from . import views

app_name='[account]'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('uploads/',views.uploads, name='uploads'),
]
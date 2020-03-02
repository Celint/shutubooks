from django.urls import path
from django.contrib import admin
from . import views

app_name = 'account'
# 目的是为了查看和修改个人信息
urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('regist/', views.regist, name='regist'),
    # path('uploads/',views.uploads, name='uploads'),
]

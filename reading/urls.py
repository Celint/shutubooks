from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('article/', views.article),
    path('detail/', views.detail),
    path('mine/', views.mine),
    path('books/', views.books)
]

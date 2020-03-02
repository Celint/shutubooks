from django.urls import path
from django.contrib import admin
from . import views
from django.conf.urls import url
from shutubooks import settings
from django.views.static import serve

app_name = 'reading'

urlpatterns = [
    path('', views.index,name='index'),#阅读首页
    # path('admin/', admin.site.urls),
    path('detail/', views.detail,name='detail'),
    path('mine/', views.mine, name='mine'),
    path('books/', views.books, name='books'),
    path('support/', views.support, name='support'),
    path('upload/',views.upload_image,name='upload')
]

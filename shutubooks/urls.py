"""shutubooks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views,settings
from django.conf.urls import url
from django.views.static import serve
# from django.conf import settings

urlpatterns = [
    path('', views.index,name='index'),
    path('admin/', admin.site.urls),    
    path('account/', include('account.urls')),
    path('reading/', include('reading.urls')),
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name = 'regist'),
    path('books/', include('books.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    #媒体文件夹，可是为什么就是跑到C盘下面了呢？？？就因为，前面多了一个'/'。
    #又来了，告诉我ac namespace没有被注册，可是我死活就是找不到
    # url(r'^upload/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT})

]

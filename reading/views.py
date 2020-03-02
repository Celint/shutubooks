from django.shortcuts import render
from account.models import stuInf
from .models import image,article
from django.shortcuts import HttpResponse,HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.
def index(request):
    user_pk = request.COOKIES.get('user_pk')
    is_login = request.COOKIES.get('is_login')
    user_obj = stuInf.objects.filter(pk=user_pk).first()
    ret={}
    if is_login:
        ret['user_name']=user_obj.stuName
    return render(request, 'index_of_reading.html',ret)
    
def detail(request):
    return render(request, 'detail_of_article.html')

def mine(request):
    return render(request, 'myarticles.html')
    
def books(request):
    return render(request, 'mybooks.html')


def support(request):
    return render(request, 'mysupport.html')

@csrf_exempt
def upload_image(request):
    imgFile = request.FILES.get('imgFile', None)
    print(imgFile)
    img = image.objects.create(image=imgFile)
    img.save()
    ret={'ret':'上传成功'}
    return HttpResponse(json.dumps(ret),content_type="application/json")

def upload_article(request):
    post = request.POST
    title_this = post.get('title')
    content_this = post.get('content')
    time = timezone.now()
    writer = post.get('writer')
    draft = post.get('draft')
    to_save = article(title=title_this, content=content_this, pub_date=time, as_draft=draft, authur=writer)
    to_save.save()
    return HttpResponse('hello')
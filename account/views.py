from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'sign.html')

def regist(requset):
    return render(requset, 'register.html')


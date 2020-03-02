from django.shortcuts import render,redirect
from account.models import stuInf
# from .models import article,image
from django.db.utils import IntegrityError
from django.shortcuts import HttpResponse,HttpResponseRedirect
import json
from django.views.decorators.csrf import ensure_csrf_cookie

def index(request):
    user_pk = request.COOKIES.get('user_pk')
    is_login = request.COOKIES.get('is_login')
    user_obj = stuInf.objects.filter(pk=user_pk).first()
    # print(user_obj)
    if is_login:
        return render(request, 'index.html', {"user_name": user_obj.stuName})
    return redirect('/login')

#这是登陆注册的view，登陆注册是在整个网站都可以用的所以。应该要拿走才对。


def login(request):
    if request.method == 'GET':
        return render(request, 'sign.html')
    elif request.method == 'POST':
        id = request.POST.get('userId')
        pw = request.POST.get('userPass')
        # print(request.POST)
        print(id)
        print(pw)
        back = {}
        user_obj = stuInf.objects.filter(stuNum=id, stuPassWord=pw).first()
        if user_obj:
            response = redirect("/")
            response.set_cookie("is_login", True)
            response.set_cookie("user_pk", user_obj.pk)
            return response
        return render(request, "sign.html", {"back": "账号或密码错误！"})
    
@ensure_csrf_cookie
def regist(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.is_ajax():
        stu = stuInf()
        print(request.POST)#这是空的啊朋友们！
        stuNum = request.POST.get('stunum')
        stuName = request.POST.get('stuname')
        stuPassWord = request.POST.get('password')
        stuCollege = request.POST.get('school')
        stuIcon = request.FILES.get('icon')
        stu.stuNum = stuNum
        stu.stuName = stuName
        stu.stuCollege = stuCollege
        stu.stuPassWord = stuPassWord
        print(stuIcon)
        if stuIcon != None:
            stu.stuImg = stuIcon
        try:
            stu.save()
        except IntegrityError as a:
            #报错，ID已经使用了
            
            back = {}
            back['msg'] = '学号已经注册过了！！请直接登录'
            # return render(request, 'register.html', context=back)
            # return render(request,context=json.dumps(back))
            return HttpResponse(json.dumps(back),content_type='application/json')
        else:
            #注册成功之后应该怎么样呢？
            back = {'msg': "注册成功，即将自动跳转！"}
            # return HttpResponse(back)
            return HttpResponse(json.dumps(back),content_type="application/json",status=201)
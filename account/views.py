from django.http import HttpResponse, response
from django.shortcuts import render

# Create your views here.
from account.models import stuInf, bookInf


def login(request):
    if request.method == 'GET':
        return render(request, 'sign.html')
    elif request.method == 'POST':
        name = request.POST.get('name1')
        pw = request.POST.get('Password1')
        try:
            stu = stuInf.objects.get(stuName=name)
            if stu.stuPassWord == pw:
                data = {
                    'is_login': True,
                    'username': stu.stuName,
                }
                response = HttpResponse('登录成功')
                response.set_cookie('usernum',stu.stuNum)
                return response
            else:
                return HttpResponse('密码错误')
        except:
            return HttpResponse('账号不存在')



def regist(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        stu = stuInf()
        stuNum = request.POST.get('num')
        stuName = request.POST.get('name1')
        stuPassWord = request.POST.get('Password1')
        stuCollege = request.POST.get('School')
        stu.stuNum = stuNum
        stu.stuName = stuName
        stu.stuCollege = stuCollege
        stu.stuPassWord = stuPassWord
        stu.save()
        return render(request, 'sign.html')


def uploads(request):
    if request.method == 'GET':
        return render(request,'uploads.html')
    elif request.method == 'POST':
        book = bookInf()
        book.bookName = request.POST.get('bookname')
        ownerNum = request.COOKIES.get('usernum')
        stu = stuInf.objects.get(stuNum=ownerNum)
        book.ownerNum = stu
        book.img = request.FILES.get('icon')
        book.type = request.POST.get('type')
        book.price = request.POST.get('price')
        book.save()
        return HttpResponse('上传成功')
    return None
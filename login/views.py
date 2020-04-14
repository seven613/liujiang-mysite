from django.shortcuts import render, redirect

from . import models
# Create your views here.
def index(request):
    pass
    return render(request,'login/index.html')

def login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        message ='请监察填写的内容!'
        if username.strip() and password:
            try:
                user = models.User.objects.get(name=username)
            except: 
                message ='用户不存在!'
                return render(request,'login/login.html',{'message':message})
            if user.password == password:
                return redirect('/login/index/')
            else:
                message ='密码不正确!'
                return render(request,'login/login.html',{'message':message})
    return render(request,'login/login.html')


def register(request):
    pass
    return render(request,'login/register.html')

def logout(request):
    pass
    return redirect('/login/')
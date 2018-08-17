import logging

from django.contrib.auth.hashers import make_password, check_password
from django.db import DatabaseError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserInfo


# Create your views here.
def login_views(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())
    else:
        uname = request.POST.get('uname')
        user = UserInfo.objects.filter(uname=uname)
        if not user:
            msgErr1 = '该用户名不存在'
            return render(request, 'login.html', locals())
        upwd = request.POST.get('upwd')
        if not check_password(upwd, user[0].upwd):
            msgErr2 = '密码错误'
            return render(request, 'login.html', locals())
        request.session['user_id'] = user[0].id
        request.session['user_name'] = user[0].uname
        return redirect('index')


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    else:
        user = UserInfo()
        user.uname = request.POST.get('uname')
        if UserInfo.objects.filter(uname=user.uname):
            msgErr1 = '用户名已存在'
            return render(request, 'register.html', locals())
        else:
            upwd = request.POST.get('upwd')
            cpwd = request.POST.get('cpwd')
            if upwd != cpwd:
                msgErr2 = '密码不一致'
                return render(request, 'register.html', locals())
            user.upwd = make_password(upwd, 'abc', 'pbkdf2_sha1')
            user.uphone = request.POST.get('uphone')
            user.uemail = request.POST.get('uemail')
            try:
                user.save()
            except DatabaseError as e:
                logging.warning(e)
                msgErr1 = '注册失败'
                return render(request, 'register.html', locals())
        user_id = UserInfo.objects.get(uname=user.uname).id
        request.session['user_id'] = user_id
        request.session['user_name'] = user.uname
        return redirect('index')

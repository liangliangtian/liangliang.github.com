# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout,login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from .models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.

#main
def index_views(request):
    return render(request, 'index.html')
#login
def index_login(request):

    if request.method == 'GET':
        return redirect('/login')
    username = request.POST.get('username')
    password = request.POST.get('password')
    isremember=request.POST.get('rem')
    try:
        user = User.objects.get(username=username)
    except:
        return HttpResponseRedirect('/')

    if check_password(password,user.password):
        a=check_password(password,user.password)
        request.session['username'] = user.username
        request.session.set_expiry(7200)
        #选择记住我创建cookie
        if isremember=='on':
            response= HttpResponseRedirect('/')
            response.set_cookie("username",user.username,3600)
            return response
        else:
            return HttpResponseRedirect('/')
    else:
        return redirect('/')


#logout
def index_logout(request):
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect('/')

#register
def index_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        user=User.objects.all()

        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        for u in user:
            if(username==u.username):
                return redirect('/')
            elif(email==u.email):
                return redirect('/')
        if password1 == password2 and username!='' and email!='' and password1!='':
            password = make_password(password1)
            user = User.objects.create(username = username,password = password, email = email)
            request.session['username'] = user.username
            request.session.set_expiry(7200)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')

#发送邮件重置密码
def index_reset(request):
    if request.method=='POST':
        username=request.POST.get('username')
        if username == '':
            return HttpResponseRedirect('/')
        else:
            user=User.objects.get(username=username)
            password=user.password
            password=password.replace('pbkdf2_sha256$36000$','a')
            send_mail("找回密码", "亲爱的用户"+username+'请点击此链接来修改你的密码,http://172.29.7.228:8000/back/reset?str1='+password+'&user='+username, "1070296285@qq.com", [user.email], fail_silently=False)
            messages.info(request,'请查看你的邮箱') 
            return HttpResponseRedirect('/')
    else:
        return redirect('/reset')
#邮件回执
def index_back(request):
    if request.method=='GET':
        password=request.GET.get('str1')
        password=password.replace(' ','+')
        username=request.GET.get('user')
        user=User.objects.get(username=username)
        user.password=password.replace('pbkdf2_sha256$36000$','a')
        if str(password) == str(user.password):
            return render(request,'back_reset.html',locals())
        else:
            messages.warning(request,'没有权限')
            return HttpResponseRedirect('/')
    else:
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1!=password2:
            messages.error(request,'两次密码不一致')
            return HttpResponse('密码不一致')
        user=User.objects.get(username=username)
        password = make_password(password1)
        user.password=password
        user.save()
        return HttpResponseRedirect('/')
#upload_video
def upload_video(request):
    print('1sdadasf')
    user_name=request.session.get('username')
    user2=User.objects.get(username=user_name)
    userid=user2.id
    if userid != '': 
        obj = request.FILES.get('inputfile')
        # samename_files=File.objects.filter(file_name=obj.name)
        # if samename_files.count()!=0:
        #     repeat_name=obj.name
        #     i=0
        #     while True:
        #         repeat_divi =str(i)+'-'
        #         repeat_name = repeat_divi + obj.name
        #         i += 1
        #         file1=File.objects.filter(file_name=repeat_name)
        #         if file1.count()==0:
        #             break
        #     messages.warning(request,'您上传的文件已存在，已为您重新命名')
        #     filename=repeat_name
        # #如果没有的文件
        # else:
        filename=obj.name
        print(filename)
        #写文件
        file_path = os.path.join('static','upload',filename)
        f = open(file_path, 'wb')
        for chunk in obj.chunks():
            f.write(chunk)
        f.close()
        print(file_path)
        File.objects.create(file_name=filename,user_id=userid,file_size=obj.size,file=file_path)
        
        return HttpResponseRedirect('/show')
        # sreturn HttpResponse('aa')
        # return render(request, 'show.html',locals())
    return HttpResponse('上传失败') 
def show_image(request):
    user_name=request.session.get('username')
    user2=User.objects.get(username=user_name)
    userid=user2.id
    files=File.objects.filter(user_id=userid).order_by('create_time').first()
    a=files.file
    a='/home/liang/myPro/liangPro/'+str(a)
    print(a)
    # l=[]
    # for file in files:
        
    #     s='/home/liang/myPro/liangPro/'+str(file.file)
    #     print(s)
    #     l.append(s)
    return render(request,'show.html',locals())

def dete1(request):
    import dete
    user_name=request.session.get('username')
    user2=User.objects.get(username=user_name)
    userid=user2.id
    files=File.objects.filter(user_id=userid).order_by('create_time').first()
    a=files.file
    a='/home/liang/myPro/liangPro/'+str(a)
    dete.runjpg1(a)
    return HttpResponseRedirect('/result')
    # return render(request,'result.html')
def result(request):
    return render(request,'result.html')

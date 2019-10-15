from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password,make_password
import json
from rbac.service.init_permission import init_permission
from rbac.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import numpy as np
from utils.custom_sort import custom_sort
import copy

class Login(View):
    def get(self,request):
        return render(request, 'home/login.html')
    def post(self,request):
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(username = u, password = p)
        if user is not None:
            if user.is_active:
                login(request,user)
                request.session['is_login'] = True
                init_permission(request,user)
                return HttpResponse(json.dumps({"status":True}))
            else:
                return HttpResponse(json.dumps({"status":False,"msg":"用户已被禁用"}))
        else:
            return HttpResponse(json.dumps({"status":False,"msg":"用户或密码错误"}))


def logout(request):
    request.session.flush()
    return redirect('/login')

class Password(LoginRequiredMixin,View):
    def get(self,request):
        return render(request, 'home/password.html')
    def post(self,request):
        old_psw = request.POST.get('oldPsw')
        new_psw = request.POST.get('newPsw')

        user_id = request.session['_auth_user_id']
        user = User.objects.get(id=user_id)
        if check_password(old_psw,user.password):
            user.password = make_password(new_psw)
            user.save()
            return HttpResponse(json.dumps({"status":True}))
        else:
            return HttpResponse(json.dumps({"status":False,"msg":"原始密码错误"}))


class UserInfo(LoginRequiredMixin,View):
    def get(self,request):
        user_id = request.session['_auth_user_id']
        user = User.objects.get(id=user_id)
        roles_str =  ','.join(user.roles.values_list('title',flat=True))
        return render(request,'home/user-info.html',{"user":user,"roles_str":roles_str})

    def post(self,request):
        user_id = request.session['_auth_user_id']
        user = User.objects.get(id=user_id)
        user.realname = request.POST.get('realname',None)
        user.email = request.POST.get('email',None)
        user.mobile = request.POST.get('mobile',None)
        user.department_id = request.POST.get('department',None)
        user.position_id = request.POST.get('position',None)
        user.signature = request.POST.get('signature',None)
        user.save()
        return HttpResponse(json.dumps({"status":True}))


class UploadHeadImg(LoginRequiredMixin,View):
    def post(self,request):
        user_id = request.session['_auth_user_id']
        user = User.objects.get(id=user_id)
        user.head_img = request.POST.get('head_img',None)
        user.save()
        return HttpResponse(json.dumps({"status": True}))

@login_required
def index(request):
    '''
        [
        {"菜单名1":[{"name":url},{"name":url}]},
        {"菜单名2":[{"name":url},{"name":url}]}
        ]
    '''
    result = []
    res = []
    user_id = request.session['_auth_user_id']
    user = User.objects.get(id=user_id)
    result = user.roles.filter(permissions__per_type=0).order_by('permissions__order_number').values_list(
        'permissions__id',
        'permissions__url',
        'permissions__parent_id',
        'permissions__title',
        'permissions__menu_icon',
        'permissions__order_number'
    ).distinct()
    result = list(result)

    result_copy = copy.deepcopy(result)
    for row in result:
        if row[2] == -1:
            res.append({
                "name": row[3],
                "id": row[0],
                "menu_icon": row[4],
                "subMenu": []
            })
            result_copy.remove(row)
    for row in result_copy:
        for i,element in enumerate(res):
            if row[2] == element['id']:
                res[i]['subMenu'].append({
                    "name": row[3],
                    "url": row[1],
                    "parent_id": row[2],
                })

    return  render(request,'home/index.html',{"user":user,"res":res})

@login_required
def console(request):
    return render(request, 'home/dashboard.html')


@login_required
def tpl_theme(request):
    return render(request,'home/tpl-theme.html')

@login_required
def tpl_note(request):
    return render(request,'home/tpl-note.html')


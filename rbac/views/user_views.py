from django.shortcuts import render,HttpResponse,redirect
from django.views import View
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rbac.serializers import *
from rest_framework.generics import ListAPIView
from utils.drf.rest_page_set import PageSet
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet
import django_filters
from django.db.models import Q
from django.contrib.auth.hashers import make_password

class UserFilter(FilterSet):
    q = django_filters.rest_framework.CharFilter(method='filter_q')
    department = django_filters.rest_framework.NumberFilter(lookup_expr="exact")

    def filter_q(self,queryset,name,value):
        return queryset.filter(Q(username__icontains=value)|Q(realname__contains=value))
    class Meta:
        model = User
        fields = ['q','department']


class UserListViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    pagination_class = PageSet

    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filter_class = UserFilter
    ordering_fields = ('username','realname','date_joined')
    ordering = ('id',)



class UserList(View):
    def get(self,request):
        authoritys = request.session.get('permissions_authoritys')
        return render(request, 'rbac/users.html',{"authoritys":authoritys})


# 修改用户状态,是否允许登录
class UpdateUserState(View):
    def post(self,request):
        uid = request.POST.get('id')
        is_active = request.POST.get('is_active')
        try:
            user = User.objects.get(id=uid)
            user.is_active = is_active
            user.save()
        except Exception as e:
            return HttpResponse(json.dumps({"status":False,"msg":"更新失败"}))
        return HttpResponse(json.dumps({"status":True,"msg":"更新成功"}))

# 删除用户
class DelUser(View):
    def post(self,request):
        uid = request.POST.get('id')
        try:
            user = User.objects.get(id=uid).delete()
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"status":False,"msg":"更新失败"}))
        return HttpResponse(json.dumps({"status":True,"msg":"更新成功"}))

# 重置用户密码为: Techfuser2019
class RestUserPassword(View):
    def post(self,request):
        uid = request.POST.get('id')
        try:
            user = User.objects.get(id=uid)
            user.password = make_password('Techfuser2019')
            user.save()
        except Exception as e:
            return HttpResponse(json.dumps({"status":False,"msg":"重置失败"}))
        return HttpResponse(json.dumps({"status":True,"msg":"重置成功,密码为:Techfuser2019"}))

# 创建用户
class CreateUser(View):
    def post(self,request):

        roles_ids = request.POST.get('roles',None)  # 字符串

        try:
            user = User.objects.create(
                username = request.POST.get('username',None),
                realname = request.POST.get('realname',None),
                department_id  = request.POST.get('department',None),
                position_id = request.POST.get('position',None),
            )

            if roles_ids:
                r = Role.objects.filter(id__in=roles_ids.split(','))
                user.roles.set(r)
        except Exception as e:
            print(e)
            return JsonResponse({"status": False, "msg": "操作失败"})

        return JsonResponse({"status":True,"msg":"操作成功"})

# 更新用户
class UpdateUser(View):
    def post(self,request):
        uid = request.POST.get('id')
        roles_ids = request.POST.get('roles',None)  # 字符串

        try:
            user = User.objects.get(id=uid)
            user.username = request.POST.get('username',None)
            user.realname = request.POST.get('realname',None)
            user.department_id  = request.POST.get('department',None)
            user.position_id = request.POST.get('position',None)
            if roles_ids:
                r = Role.objects.filter(id__in=roles_ids.split(','))
                user.roles.set(r)
            user.save()
        except Exception as e:
            print(e)
            return JsonResponse({"status": False, "msg": "操作失败"})

        return JsonResponse({"status":True,"msg":"操作成功"})
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
from rbac.models import Permission
from rest_framework.pagination import PageNumberPagination




class PermissionListViewSet(ListAPIView):
    class PermPagination(PageNumberPagination):
        page_size = 100
        max_page_size = 100
    queryset = Permission.objects.all().order_by('order_number')
    serializer_class = PermissionModelSerializer
    pagination_class = PermPagination

class PermissionList(View):
    def get(self,request):
        return render(request, 'rbac/permissions.html')



# 创建权限菜单
class CreatePermission(View):
    def post(self,request):
        try:
            per = Permission.objects.create(
                title = request.POST.get('title',None),
                url = request.POST.get('url',None),
                parent_id  = request.POST.get('parent_id',None),
                per_type = request.POST.get('per_type',None),
                authority=request.POST.get('authority', None),
                order_number=request.POST.get('order_number', None),
                menu_icon=request.POST.get('menu_icon', None),
            )
        except Exception as e:
            print(e)
            return JsonResponse({"status": False, "msg": "操作失败"})

        return JsonResponse({"status":True,"msg":"操作成功"})

# 更新权限菜单
class UpdatePermission(View):
    def post(self,request):
        pid = request.POST.get('id')
        try:
            per = Permission.objects.get(id=pid)
            per.title = request.POST.get('title', None)
            per.url = request.POST.get('url', None)
            per.parent_id = request.POST.get('parent_id', None)
            per.per_type = request.POST.get('per_type', None)
            per.authority = request.POST.get('authority', None)
            per.order_number = request.POST.get('order_number', None)
            per.menu_icon = request.POST.get('menu_icon', None)
            per.save()
        except Exception as e:
            print(e)
            return JsonResponse({"status": False, "msg": "操作失败"})

        return JsonResponse({"status":True,"msg":"操作成功"})

class DeletePermission(View):
    def post(self,request):
        pid = request.POST.get('id')
        try:
            Permission.objects.get(id=pid).delete()

        except Exception as e:
            print(e)
            return JsonResponse({"status": False, "msg": "操作失败"})

        return JsonResponse({"status":True,"msg":"操作成功"})
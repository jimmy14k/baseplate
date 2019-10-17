from django.shortcuts import render,HttpResponse,redirect
from rest_framework.generics import ListAPIView
from utils.drf.rest_page_set import PageSet
from rbac.models import Role,Permission
from rbac.serializers import RoleModelSerializer
from rest_framework.filters import OrderingFilter,SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import FilterSet
import django_filters
from django.db.models import Q
from django.views import View
from django.http import JsonResponse
import json
from django.db.models import F
import logging
logger = logging.getLogger(__name__)



class RoleFilter(FilterSet):
    q = django_filters.rest_framework.CharFilter(method='filter_q')

    def filter_q(self,queryset,name,value):
        return queryset.filter(Q(title__icontains=value))
    class Meta:
        model = Role
        fields = ['q',]

class RoleListViewSet(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer
    pagination_class = PageSet

    filter_backends = (DjangoFilterBackend,OrderingFilter)
    filter_class = RoleFilter
    ordering = ('id',)

class RoleList(View):
    def get(self,request):
        authoritys = request.session.get('permissions_authoritys')
        return render(request, 'rbac/roles.html',{"authoritys":authoritys})

class CreateRole(View):
    def post(self,request):
        try:
            Role.objects.create(
                title=request.POST.get('title', None),
                comment=request.POST.get('comment', None),
            )
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status": False, "msg": "创建失败"})

        return JsonResponse({"status": True, "msg": "创建成功"})

class UpdateRole(View):
    def post(self,request):
        rid = request.POST.get('id')
        try:
            user = Role.objects.get(id=rid)
            user.title = request.POST.get('title')
            user.comment = request.POST.get('comment')
            user.save()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"更新失败"})
        return JsonResponse({"status":True,"msg":"更新成功"})

class DeleteRole(View):
    def post(self,request):
        rid = request.POST.get('id')
        try:
            Role.objects.get(id=rid).delete()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"删除失败"})
        return JsonResponse({"status":True,"msg":"删除成功"})

# 获取角色的权限
class GetRolePermissions(View):
    def post(self,request):
        rid = request.POST.get('id')
        result = []
        per_all = Permission.objects.all().values('id','title','parent_id','authority','per_type')

        cur_role_obj = Role.objects.get(id=rid)
        cur_role_per = cur_role_obj.permissions.all().values_list('id',flat=True)

        for row in per_all:
            dic = {
                "pId": row['parent_id'],
                "id": row['id'],
                "open": True,
            }
            if row['per_type'] == 0:
                dic["name"] = row['title'] + ' 『Menu』'
            elif row['per_type'] == 1:
                dic["name"] = row['title'] + ' 『Button』'
            else:
                dic["name"] = row['title'] + ' 『Api』'
            if row['id'] in cur_role_per:
                dic["checked"]= True
            else:
                dic["checked"] = False
            result.append(dic)

        return HttpResponse(json.dumps(result))

# 更新角色的权限
class UpdateRolePermissions(View):
    def post(self,request):
        rid = request.POST.get('id')
        auth_ids = request.POST.get('authIds')
        try:
            role = Role.objects.get(id=rid)
            role.permissions.set(eval(auth_ids))
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"更新失败"})
        return JsonResponse({"status": True, "msg": "更新成功"})
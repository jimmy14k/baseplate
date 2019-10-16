from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from rest_framework.generics import ListAPIView
from rbac.models import Department,Position
from rbac.serializers import DepartmentModelSerializer,PositionModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse


import logging
logger = logging.getLogger(__name__)

class OthersPage(View):
    def get(self,request):
        return render(request, 'rbac/others.html')

# 部门信息
class DepartmentListViewSet(ListAPIView):
    class PermPagination(PageNumberPagination):
        page_size = 10000
        max_page_size = 100
    queryset = Department.objects.all().order_by('id')
    serializer_class = DepartmentModelSerializer
    pagination_class = PermPagination

# 新增部门
class CreateDepartment(View):
    def post(self,request):
        try:
            Department.objects.create(
                name=request.POST.get('name'),
            )
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status": False, "msg": "创建失败"})

        return JsonResponse({"status": True, "msg": "创建成功"})

# 更新部门
class UpdateDepartment(View):
    def post(self,request):
        did = request.POST.get('id')
        try:
            user = Department.objects.get(id=did)
            user.name = request.POST.get('name')
            user.save()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"更新失败"})
        return JsonResponse({"status":True,"msg":"更新成功"})

# 删除部门
class DeleteDepartment(View):
    def post(self,request):
        did = request.POST.get('id')
        try:
            Department.objects.get(id=did).delete()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"删除失败"})
        return JsonResponse({"status":True,"msg":"删除成功"})


# 岗位信息
class PositionListViewSet(ListAPIView):
    class PermPagination(PageNumberPagination):
        page_size = 10000
        max_page_size = 100
    queryset = Position.objects.all().order_by('id')
    serializer_class = DepartmentModelSerializer
    pagination_class = PermPagination

# 新增岗位
class CreatePosition(View):
    def post(self,request):
        try:
            Position.objects.create(
                name=request.POST.get('name'),
            )
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status": False, "msg": "创建失败"})

        return JsonResponse({"status": True, "msg": "创建成功"})

# 更新岗位
class UpdatePosition(View):
    def post(self,request):
        print(request.POST)
        pid = request.POST.get('id')
        try:
            user = Position.objects.get(id=pid)
            user.name = request.POST.get('name')
            user.save()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"更新失败"})
        return JsonResponse({"status":True,"msg":"更新成功"})

# 删除岗位
class DeletePosition(View):
    def post(self,request):
        pid = request.POST.get('id')
        try:
            Position.objects.get(id=pid).delete()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"删除失败"})
        return JsonResponse({"status":True,"msg":"删除成功"})
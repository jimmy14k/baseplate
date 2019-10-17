from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from rest_framework.generics import ListAPIView
from rbac.models import Department,Position,DevLanguage
from rbac.serializers import DepartmentModelSerializer,PositionModelSerializer,DevLangModelSerializer
from rest_framework.pagination import PageNumberPagination
from django.http import JsonResponse


import logging
logger = logging.getLogger(__name__)

class ConfigPage(View):
    def get(self,request):
        authoritys = request.session.get('permissions_authoritys')
        return render(request, 'rbac/config.html',{"authoritys":authoritys})

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
    serializer_class = PositionModelSerializer
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


# 开发语言信息
class DevLangViewSet(ListAPIView):
    class PermPagination(PageNumberPagination):
        page_size = 10000
        max_page_size = 100
    queryset = DevLanguage.objects.all().order_by('id')
    serializer_class = DevLangModelSerializer
    pagination_class = PermPagination

# 新增开发语言
class CreateDevLang(View):
    def post(self,request):
        try:
            DevLanguage.objects.create(
                name=request.POST.get('name'),
            )
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status": False, "msg": "创建失败"})

        return JsonResponse({"status": True, "msg": "创建成功"})

# 更新开发语言
class UpdateDevLang(View):
    def post(self,request):
        pid = request.POST.get('id')
        try:
            user = DevLanguage.objects.get(id=pid)
            user.name = request.POST.get('name')
            user.save()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"更新失败"})
        return JsonResponse({"status":True,"msg":"更新成功"})

# 删除开发语言
class DeleteDevLang(View):
    def post(self,request):
        pid = request.POST.get('id')
        try:
            DevLanguage.objects.get(id=pid).delete()
        except Exception as e:
            logger.error(str(e))
            return JsonResponse({"status":False,"msg":"删除失败"})
        return JsonResponse({"status":True,"msg":"删除成功"})
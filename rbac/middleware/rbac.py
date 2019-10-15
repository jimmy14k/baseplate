import re
from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django_redis import get_redis_connection
from rbac.service.init_permission import init_permission
from rbac.models import User
import json


class RbacMiddleware(MiddlewareMixin):
    def process_request(self, request):
        #判断权限是否更新
        conn = get_redis_connection()
        user_or_role_update_counter = conn.hget('user_or_role_update', 'counter')
        if not user_or_role_update_counter:
            user_or_role_update_counter = 0
        try:
            session_counter = request.session['userinfo']['user_or_role_update_counter']
        except:
            session_counter = 0
        if int(user_or_role_update_counter) > int(session_counter):
            try:
                user = User.objects.get(id=request.session.get('_auth_user_id'))
                init_permission(request,user)
            except Exception as e:
                pass

        current_url = request.path_info
        valid_urls = settings.VALID_URLS

        # 1.判断当前请求url是否在白名单
        for url in valid_urls:
            if re.match(url,current_url):
                return None

        permissions_urls = request.session.get('permissions_urls')

        # 2.验证是否已经登录
        if not permissions_urls:
            return redirect('/login')

        # 3. 与当前访问的url与权限url进行匹配验证,并在request中写入权限标识信息
        #  一是用来判断用户有权限请求当前url
        #  二是如果请求的是一个页面，页面中有些按钮需要根据权限进行屏蔽
        flag = False
        for url in permissions_urls:
            regax = '^{0}$'.format(url)
            if re.match(regax, current_url):
                flag = True
                break
        if not flag:
            return HttpResponse(json.dumps({"status":False,"msg":"没有权限"}))

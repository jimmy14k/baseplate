from django.conf import settings
from django_redis import get_redis_connection

def init_permission(request,user):
    '''
    用户登录时,初始化权限,将权限放到session中
    :param request:  当前请求
    :param user:  当前登录用户,object
    :return:  None
    '''

    # 拿到用户的所有权限信息
    permission_url_list = user.roles.values(
        'permissions__url',          # url
        'permissions__authority',    # 权限标识
    ).distinct()

    permissions_urls = []
    permissions_authoritys = []
    for row in permission_url_list:
        if row['permissions__url']:
            permissions_urls.append(row['permissions__url'])
        if row['permissions__authority']:
            permissions_authoritys.append(row['permissions__authority'])

    # 写入session
    request.session['permissions_urls'] = permissions_urls
    request.session['permissions_authoritys'] = permissions_authoritys
    #权限变化更新
    conn = get_redis_connection()
    user_or_role_update_counter = conn.hget('user_or_role_update', 'counter')
    if not user_or_role_update_counter:
        user_or_role_update_counter = 0
    request.session['user_or_role_update_counter'] = user_or_role_update_counter
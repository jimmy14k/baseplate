from django.urls import path
from .views.user_views import *
from .views.permission_views import *
from .views.role_views import *

app_name = "assets"

urlpatterns = [
    path('user-list',UserList.as_view(),name='user-list'),
    path('users',UserListViewSet.as_view(),name='users'),

    path('update-user-state',UpdateUserState.as_view(),name='update-user-state'),  #更新用户状态
    path('del-user',DelUser.as_view(),name='del-user'),                            #删除用户
    path('rest-psw',RestUserPassword.as_view(),name='rest-psw'),                   #重置密码
    path('create-user',CreateUser.as_view(),name='create-user'),                   #创建用户
    path('update-user',UpdateUser.as_view(),name='update-user'),                   #更新用户


    path('permission-list',PermissionList.as_view(),name='permission-list'),
    path('permissions',PermissionListViewSet.as_view(),name='permissions'),
    path('update-per',UpdatePermission.as_view(),name='update-per'),               #更新权限
    path('create-per',CreatePermission.as_view(),name='create-per'),               #创建权限
    path('delete-per',DeletePermission.as_view(),name='delete-per'),               #删除权限

    path('role-list',RoleList.as_view(),name='role-list'),
    path('roles',RoleListViewSet.as_view(),name='roles'),
    path('create-role',CreateRole.as_view(),name='create-role'),                    #创建角色
    path('update-role',UpdateRole.as_view(),name='create-role'),                    #更新角色
    path('delete-role',DeleteRole.as_view(),name='create-role'),                    #删除角色
    path('get-role-permissions',GetRolePermissions.as_view(),name='get-role-permissons'),            #获取角色权限
    path('update-role-permissions',UpdateRolePermissions.as_view(),name='update-role-permissions'),  #更新角色权限
]
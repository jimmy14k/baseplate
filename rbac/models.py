from django.db import models
from django.contrib.auth.models import AbstractUser
from django_redis import get_redis_connection

class Department(models.Model):
    name = models.CharField(max_length=128, verbose_name='部门名称',unique=True)
    class Meta:
        db_table = 'department'
        verbose_name = "部门表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Position(models.Model):
    name = models.CharField(max_length=128, verbose_name='职位名称',unique=True)
    class Meta:
        db_table = 'position'
        verbose_name = "职位表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name


class Permission(models.Model):
    '''
    权限表
    '''
    TYPE_CHOICES = (
        (0,'菜单'),
        (1,'按钮'),
        (2,'接口'),
    )
    title = models.CharField(max_length=32,verbose_name='权限名称')
    url = models.CharField(max_length=128,verbose_name='URL',blank=True,null=True,unique=True)
    parent_id = models.IntegerField(verbose_name='上级菜单ID',blank=True,null=True,default=-1)
    per_type = models.IntegerField(choices=TYPE_CHOICES,verbose_name='权限类型')
    authority = models.CharField(verbose_name='权限标识',max_length=64,blank=True,null=True)
    order_number = models.IntegerField(verbose_name='序号',blank=True,null=True)
    menu_icon = models.CharField(max_length=64,verbose_name='菜单图标',blank=True,null=True)
    c_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    u_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)

    class Meta:
        db_table = 'permission'
        verbose_name = "权限表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        conn = get_redis_connection()
        conn.hincrby('user_or_role_update', 'counter')
        super(Permission, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)

class Role(models.Model):
    '''
    角色
    '''
    title = models.CharField(max_length=32,verbose_name='角色名称',unique=True)
    comment = models.TextField(verbose_name='备注',blank=True,null=True)
    permissions = models.ManyToManyField(Permission,verbose_name='角色权限',blank=True,related_name='role_permissions')
    c_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间', blank=True)
    u_time = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间', blank=True)
    class Meta:
        db_table = 'role'
        verbose_name = "角色表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.title
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        conn = get_redis_connection()
        conn.hincrby('user_or_role_update', 'counter')
        super(Role, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)


class User(AbstractUser):
    '''
    用户
    '''
    realname = models.CharField(max_length=32, verbose_name='姓名',blank=True,null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,verbose_name='部门',blank=True,null=True)
    position = models.ForeignKey(Position,on_delete=models.SET_NULL, verbose_name='职位',blank=True,null=True)
    mobile = models.CharField(max_length=32, verbose_name='手机', blank=True, null=True)
    signature = models.CharField(max_length=32, verbose_name='签名', blank=True, null=True)
    head_img = models.TextField(verbose_name='用户图像',blank=True,null=True)
    roles = models.ManyToManyField(Role,verbose_name='用户角色',blank=True,related_name='user_roles')

    class Meta:
        db_table = 'user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.username
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        conn = get_redis_connection()
        conn.hincrby('user_or_role_update', 'counter')
        super(User, self).save(force_insert=False, force_update=False, using=None,
             update_fields=None)
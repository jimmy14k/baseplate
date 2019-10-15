from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('realname', 'mobile', 'email','department','position','signature')}),
        (_('Roles'), {'fields': ('roles',)}),
        (_('Other Info'), {'fields': ('is_active', 'is_staff', 'is_superuser','last_login', 'date_joined')}),
    )
    list_display = ('username', 'realname', 'department', 'position', 'is_active','is_staff')



admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(User,CustomUserAdmin)
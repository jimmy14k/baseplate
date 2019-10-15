from rbac.models import Department,Position,Role,Permission
from django import template
from django.forms.models import model_to_dict

register = template.Library()

@register.filter(name='dep_choices')
def dep_choices(value):
    deps = Department.objects.all()
    return deps

@register.filter(name='positions_choices')
def positions_choices(value):
    p = Position.objects.all()
    return p

@register.filter(name='roles_choices')
def roles_choices(value):
    r = Role.objects.all()
    return r

@register.filter(name='menu_choices')
def menu_choices(value):
    p = Permission.objects.filter(per_type=0)
    return p
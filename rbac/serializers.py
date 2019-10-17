from rbac.models import User,Permission,Role,Department,Position,DevLanguage
from rest_framework import serializers


class RoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
class DepartmentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ("id","name")
class PositionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ("id","name")
class DevLangModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevLanguage
        fields = ("id","name")

class UserModelSerializer(serializers.ModelSerializer):
    roles = RoleModelSerializer(many=True)
    department = DepartmentModelSerializer()
    position = PositionModelSerializer()
    class Meta:
        model = User
        fields = ("id","username","realname","department","position","mobile","roles","date_joined","is_active")


class PermissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
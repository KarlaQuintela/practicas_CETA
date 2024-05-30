from rest_framework import serializers
from models import User,Role

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','fk_id_role')

class RoleSerializer(serializers.Serializer):
    class Meta:
        model = Role
        fields = ['name_role']
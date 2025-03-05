from django.contrib.auth.models import User
from rest_framework import serializers

from .models import MasterAuth, UserAuth,AuthUser


# class CustomDateTimeField(serializers.ReadOnlyField, ABC):
#     def to_representation(self, value):
#         return value.date() if value else None


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'id']


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuth
        fields = '__all__'


class MasterAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterAuth
        fields = '__all__'

class MasterAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'



class AuthListSerializer(serializers.ModelSerializer):
    user = AuthSerializer()
    auth = MasterAuthSerializer()

    class Meta:
        model = UserAuth
        fields = ['id', 'status', 'auth', 'updated_at', 'user', 'user', 'auth']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
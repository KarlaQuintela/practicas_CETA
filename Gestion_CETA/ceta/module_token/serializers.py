from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

def add_custom_claims(token,user: User):
    token['name'] = user.username
    token['role'] = user.groups.first().name
    return token


class TokenObtain(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: User) -> Token:
        token = super().get_token(user)
        token = cls.add_claims(cls,token,user)
        return token
    def add_claims(self,token,user):
        return token


class MyTokenObtainPairSerializer(TokenObtain):
    def add_claims(self, token, user):
        return add_custom_claims(token,user)

class MyRefreshTokenObtainSerializer(TokenObtain):
    def add_claims(self, token, user):
        return add_custom_claims(token,user)
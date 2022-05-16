from rest_framework import serializers
from rest_framework.authtoken.models import Token


# 로그인
class LoginSerializers(serializers.Serializer) :
    username = serializers.CharField
    password = serializers.CharField()

# 토큰
class TokenSerializers(serializers.ModelSerializer) :
    class Meta :
        model = Token
        fields = ['key']


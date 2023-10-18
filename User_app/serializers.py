#import serializers
from rest_framework import serializers
from .models import User, Password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        #fields all
        fields = '__all__'
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
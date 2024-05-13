from rest_framework import serializers
from p1App.models import *
from django.contrib.auth import authenticate

class RegSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUserdb
        fields=['username','full_name','email','mobile','password']


class Loginserializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError("Incorrect username or password")

        attrs['user'] = user
        return attrs

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectdb
        fields = "__all__"
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorydb
        fields = "__all__"

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectupdatedb
        fields = "__all__"
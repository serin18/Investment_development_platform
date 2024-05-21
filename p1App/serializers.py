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
<<<<<<< HEAD
    
=======
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projectdb
<<<<<<< HEAD
        fields = "__all__"
=======
        fields = ['id','project_name','description','category','amount','end_date','image']
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorydb
        fields = "__all__"
<<<<<<< HEAD
    
=======

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectupdatedb
        fields = "__all__"
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f

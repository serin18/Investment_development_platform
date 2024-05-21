from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status,permissions,authentication


authentication_classes = [authentication.BasicAuthentication]
permission_classes = [permissions.IsAuthenticated]
     



class CatogaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        
class ProjectApi(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)


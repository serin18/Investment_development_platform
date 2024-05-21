from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status



class ProjectList(APIView):
    def get(self,request,*args,**kwargs):
          project=Projectdb.objects.all()
          return Response({"project":project})
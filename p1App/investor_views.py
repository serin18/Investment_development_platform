from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions,authentication

class ProjectView(APIView):

    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Retrieve projects uploaded by the currently authenticated user
        projects = Projectdb.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        projects = Projectdb.objects.filter(id=id)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
        

    
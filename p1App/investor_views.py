from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions,authentication
from django.core.exceptions import ValidationError


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
        
class ProfileUpdate(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = self.request.user.id
        try:
            profile = CustomUserdb.objects.get(id=user)
        except Projectdb.DoesNotExist:
            return Response(data={"message": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = CustomUserdbSerializer(instance=profile, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = self.request.user.id
        profile=CustomUserdb.objects.filter(id=user)
        serializer = CustomUserdbSerializer(profile,many=True)
        return Response(serializer.data)
    
class NotificationView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        try:
            qs = Projectdb.objects.get(id=id)
        except Projectdb.DoesNotExist:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.validated_data['sender'] = request.user
                serializer.save(receiver=qs.inovator, project=qs)
                return Response(data=serializer.data)
            except ValidationError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

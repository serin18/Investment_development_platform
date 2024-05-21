from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework import status,permissions,authentication


authentication_classes = [authentication.BasicAuthentication]
permission_classes = [permissions.IsAuthenticated]
     



class CatogaryView(APIView):
    permission_classes = [permissions.IsAuthenticated]
=======
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions,authentication

class CatogariView(APIView):
    
    def get(self,request,*args,**kwargs):
        category=Categorydb.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(data = serializer.data)
    
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f
    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        
class ProjectApi(APIView):
<<<<<<< HEAD
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,*args,**kwargs):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
=======
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.validated_data['inovator'] = request.user
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        
    def get(self, request, *args, **kwargs):
        # Retrieve projects uploaded by the currently authenticated user
        projects = Projectdb.objects.filter(inovator_id=request.user)
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            project = Projectdb.objects.get(id=id)
        except Projectdb.DoesNotExist:
            return Response(data={"message": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProjectSerializer(instance=project, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = Projectdb.objects.get(id=pk)
        if project:
            project.delete()
            return Response("project removed")
        else:
            return Response("project does not exist")
    

class UpdateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post (self,request,*args,**kwargs):
        serializer = UpdateSerializer(data = request.data)
        if serializer.is_valid():
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
<<<<<<< HEAD

=======
        
    
>>>>>>> f6a76b6aeb9cd02726da79bdb8c653eeead6875f

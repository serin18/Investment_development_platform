from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework import status,permissions,authentication

class CatogariView(APIView):
    
    def get(self,request,*args,**kwargs):
        category=Categorydb.objects.all()
        serializer=CategorySerializer(category,many=True)
        return Response(data = serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer = CategorySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        
class ProjectApi(APIView):
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

    def post(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        
        try:
            qs = Projectdb.objects.get(id=id)
        except Projectdb.DoesNotExist:
            return Response({"error": "Project not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UpdateSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(project_name=qs)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
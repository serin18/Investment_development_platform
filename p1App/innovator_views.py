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
    
    # def delete(self, request, pk):
    #     try:
    #         project = Projectdb.objects.get(id=pk)
    #     except Projectdb.DoesNotExist:
    #         return Response(data={"message": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
    #     if project.active:
    #         return Response(data={"message": "Cannot delete an active project"}, status=status.HTTP_400_BAD_REQUEST)
        
    #     if project.can_delete():
    #         project.delete()
    #         return Response(data={"message": "Project deleted successfully"}, status=status.HTTP_200_OK)
    #     else:
    #         return Response(data={"message": "Cannot delete project with transactions"}, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post (self,request,*args,**kwargs):
        serializer = UpdateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        else:
            return Response(data = serializer.errors)
        
    
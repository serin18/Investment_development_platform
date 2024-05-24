from rest_framework.views import APIView
from p1App.models import *
from p1App.serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login,logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
<<<<<<< HEAD
from rest_framework.authentication import TokenAuthentication
=======
from rest_framework import viewsets
>>>>>>> 2c68e8e (messgage)



class InnovatorReg(APIView):
    serializer_class=RegSerializer
    def post(self,request):
        serializer=RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_innovator'] = True
            user = CustomUserdb.objects.create_user(**serializer.validated_data)
            return Response({'message': 'registered successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class InvesterReg(APIView):
    serializer_class=RegSerializer
    def post(self,request):
        serializer=RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['is_investor'] = True
            user = CustomUserdb.objects.create_user(**serializer.validated_data)
            return Response({'message': 'registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    serializer_class= Loginserializer
    def post(self, request):
        serializer = Loginserializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            data = {
                'id': user.id,
                'username': user.username,
                'is_innovator': user.is_innovator,
                'is_investor': user.is_investor,
            }
            token, created = Token.objects.get_or_create(user=user)
            return Response({'message': 'logged in successfully', 'token': token.key, 'data': data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        
        logout(request)

        
        try:
            token = request.auth
            token.delete()
        except (AttributeError, Token.DoesNotExist):
            pass

        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
    
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messagedb.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        sender = request.user
        receiver_id = request.data.get('receiver')
        project_id = request.data.get('project')
        message = request.data.get('message')

        receiver = CustomUserdb.objects.get(pk=receiver_id)
        project = Projectdb.objects.get(pk=project_id)

        msg = Messagedb.objects.create(sender=sender, receiver=receiver, project=project, message=message)
        serializer = self.get_serializer(msg)
        return Response(serializer.data)
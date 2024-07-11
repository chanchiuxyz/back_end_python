from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#REST framework
from rest_framework import permissions,viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Users,User
from django_api.serializers import UserSerializer,UsersSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token


# Create your views here.

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED)

def index(request) :
    return HttpResponse('django_api pages')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # username = request.query_params.get('username',None)
    # queryset = User.objects.filter(username=username)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def username(self,request, pk=None):
        # se = self.get_object()
        # print('request',se)
        # print('request',self)
        user = get_object_or_404(User, username=pk)

        result = {
            'username': user.username,
            'password': user.password,

        }

        return Response(result, status=status.HTTP_200_OK)
# class UserViewGet(viewsets.ModelViewSet):
#     # queryset = User.objects.get(username='admin')
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

    
    @action(detail=False, methods=['post'])
    def getuser(self, request):
        username = request.query_params.get('username',None)
        password = request.query_params.get('password',None)
        print(password)
        user = get_object_or_404(User, username=username)
        result = {
            '_id': str(user._id),
            'username': user.username,
            'password': user.password,
            'phone': user.phone,
            'email': user.email,

        }
        print(result)
        if (result['username'] == username and result['password'] == password):
            response = {'status': 0 , 'data':result}
        else:
            response = {'status': 1 , 'data': 'error'}

        print(result['password'])
        print(password)
        return Response(response)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = [permissions.IsAuthenticated]

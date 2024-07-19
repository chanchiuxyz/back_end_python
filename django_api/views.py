from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

#REST framework
from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework import permissions,viewsets,status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Users, Roles, Categories, Products
from django_api.serializers import UsersSerializer, RolesSerializer, CategoriesSerializer, ProductsSerializer, GetUserSerializer
from rest_framework.views import APIView, View
# from rest_framework.generics import GenericAPIView, RetrieveAPIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
# md5
import hashlib
from django_filters import rest_framework as filters

# from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.conf import settings
from django.http import JsonResponse

# Create your views here.

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # data = json.load(request.body)
        # print(request.body)
        username = request.data.get('username')
        password = request.data.get('password')
  
        user = authenticate(request, username=username, password=password)
        print('us',user)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'status':0 , 'data':{'token': token.key}})
        return Response({'error': 'Invalid Credentials'}, status=400)

def index(request) :
    return HttpResponse('django_api pages')



# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     @action(detail=True, methods=['get'])
#     def login(self,request, username=None):
#         ususernameer = request.query_params.get('username')
#         if not username:
#             return Response({'error': 'username query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             item = User.objects.get(username=username)
#         except User.DoesNotExist:
#             return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = UsersSerializer(item)
#         return Response(serializer.data)
# get user by username
class GetUserViewSet(generics.RetrieveAPIView,APIView) :
    # serializer_class = GetUserSerializer

    def get(self, request, name, *args, **kwargs):
        try:
            user = Users.objects.get(username=name)
            serializer = GetUserSerializer(user,context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Users.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, UsersSerializer):
        # md5 password
        data = UsersSerializer.validated_data
        data['password'] = hashlib.md5(data['password'].encode()).hexdigest()
        
        # save
        UsersSerializer.save(**data)
    @action(detail=False, methods=['post'])
    @csrf_exempt
    def getuser(self, request):
        # get params from request body
        username = request.data.get('username',None)
        password = request.data.get('username',None)
        # get params from url
        # ususernameer = request.query_params.get('username')
        try :
            user = Users.objects.get(username=username)
        except :
            return Response({'status': 1 , 'data': 'user not exist'})
        print(user.username,user.password)
        # get params from url
        # instance = User.query_params.get(username=username)
        serializer = UsersSerializer(user,context={'request': request})
        password = hashlib.md5(password.encode()).hexdigest()
        if (user.username == username and user.password == password):
            response = {'status': 0 , 'data':serializer.data}
        else:
            response = {'status': 1 , 'data': serializer.error_messages}
        return Response(response)
class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
# FilterSet tutorial:
# https://django-filter.readthedocs.io/en/stable/guide/rest_framework.html
class CategoriesFilter(filters.FilterSet):
    parentId = filters.CharFilter(field_name="parentId", lookup_expr='exact')
    # max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    class Meta:
        model = Categories
        fields = ['parentId']
class CategoriesViewSet(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    # print('cate')
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # filter
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CategoriesFilter
    # permission_classes = [permissions.AllowAny]  # Ensure you have the correct permissions

    # def patch(self) :
    #     return Response({'patch': 'django'})


# class TestViewSet(View):
#     # queryset = Products.objects.all()
#     def get(self, request,name) :
#         category = Categories.objects.get(name=name)
#         serializer_class = CategoriesSerializer
#         # permission_classes = [permissions.IsAuthenticated]
#         # authentication_classes = [TokenAuthentication]
#         # permission_classes = [permissions.IsAuthenticated]
#         serializer = CategoriesSerializer(instance=category)
#         return Response(serializer.data)

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def upload_image(request):
    # print('upload')
    # print(request)
    # return HttpResponse('Image uploaded successfully.')
    file = request.FILES['image']
    root = '%s\%s'%(settings.PICUTRES, file.name)
    with open(root, 'wb') as f:
        for i in file.chunks():
            f.write(i)
    response = {'status': 0 , 'data': {'name':file.name}}
    # response = json.load(response)
    return JsonResponse(data=response)
# def get_csrf(request):
#         #generate csrf send to front-end 
#     x = csrf(request)
#     csrf_token = x['csrf_token']
#     return HttpResponse('{} ; {}'.format('csrf_token', csrf_token))
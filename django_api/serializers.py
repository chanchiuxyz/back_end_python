from rest_framework import serializers
from .models import Users,User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['_id','username','password','phone','email','role_id','create_time']

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['_id','username','password','phone','email','role_id','create_time']
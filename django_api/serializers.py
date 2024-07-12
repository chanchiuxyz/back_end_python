from rest_framework import serializers
from .models import Users,User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # 自定义字段输出格式
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # 例如，把日期格式化为字符串
        data['_id'] = str(instance._id)
        return data

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['_id','username','password','phone','email','role_id','create_time']
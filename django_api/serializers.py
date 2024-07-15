from rest_framework import serializers
from .models import Users, Roles, Categories, Products

class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # _id int to str
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # _id int to str
        data['_id'] = str(instance._id)
        return data
    
class GetUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        # fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # _id int to str
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # _id int to str
        data['_id'] = str(instance._id)
        return data
    
class RolesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'
        # fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # _id int to str
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # _id int to str
        data['_id'] = str(instance._id)
        return data
class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        # fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # _id int to str
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # _id int to str
        data['_id'] = str(instance._id)
        return data
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
        # fields = ['_id' ,'username','password','phone','email','role_id','create_time']
            # _id int to str
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # _id int to str
        data['_id'] = str(instance._id)
        return data
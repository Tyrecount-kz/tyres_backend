from rest_framework import serializers
from users.models import ShopUser
from shop.models import Car
from shop.api.serializers import CarSerializer

class ShopUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShopUser
        exclude = ['password']
        read_only_field = ['id','first_name','last_name']
    
class ShopUserPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
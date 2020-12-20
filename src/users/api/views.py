from django.shortcuts import render
from .serializers import ShopUserSerializer,ShopUserPostsSerializer
from rest_framework import generics,mixins
from users.models import ShopUser
from shop.models import Car
from shop.api.serializers import CarSerializer

# Create your views here.
class ShopUserRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ShopUserSerializer
    
    def get_queryset(self):
        qs = ShopUser.objects.all()
        return qs

class ShopUserListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ShopUserSerializer

    def get_queryset(self):
        qs = ShopUser.objects.all()
        return qs

class ShopUserPostsListView(generics.ListAPIView):  
    lookup_field = 'pk'
    serializer_class = ShopUserPostsSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        print(user_id)
        return Car.objects.all().filter(user_id=user_id)
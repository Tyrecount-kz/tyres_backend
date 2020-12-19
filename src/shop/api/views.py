from rest_framework import generics, mixins
from shop.models import Car
from .serializers import PostSerializer, CarSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated,IsAuthenticatedOrReadOnly, SAFE_METHODS
from django.db.models import Q

class ShopCarRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Car.objects.all() 


class ShopCarAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        qs = Car.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            """ for postgres
            qs = Car.objects.annotate(
                search=SearchVector('car_model') + SearchVector('user_id') 
                                                 + SearchVector('shell') 
                                                 + SearchVector('color')
                                                 + SearchVector('custom_clear')
                                                 + SearchVector('custom_clear')
                                                 + SearchVector('gear')
                                                 + SearchVector('city')
            ).filter(search=query"""
            qs = qs.filter(Q(car_model__icontains=query) | Q(shell_icontains=query) | Q(city_icontains=query)).distinct()
        return qs

from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator,MinValueValidator

User = settings.AUTH_USER_MODEL

# Create your models here.
class Car(models.Model):
    user_id = models.ForeignKey(User, default=1, null=True,on_delete=models.CASCADE)
    car_model = models.CharField(max_length=150,null=True)
    release_year = models.DateTimeField(null=True)
    shell = models.CharField(max_length=150,null=True)
    mileage = models.IntegerField(null=True)
    transmission = models.CharField(max_length=150,null=True)
    rudder = models.CharField(max_length=60,null=True)
    color = models.CharField(max_length=150,null=True)
    gear = models.CharField(max_length=150,null=True)
    custom_clear = models.CharField(max_length=150,null=True)
    price = models.CharField(max_length=150,null=True)
    engine_volume = models.CharField(max_length=150,null=True)
    city = models.CharField(max_length=250,null=True)

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return self.car_model

class Post(models.Model):
    car_id = models.ForeignKey(Car, null=True,on_delete=models.CASCADE)
    post_name = models.CharField(max_length=300,null=True)
    post_description = models.TextField(null=True)
    user_id = models.ForeignKey(User, default=1, null=True,on_delete=models.CASCADE)
    views = models.IntegerField(null=True)
    added_to_wishlist = models.IntegerField(null=True,validators=[MaxValueValidator(1),MinValueValidator(0)])
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

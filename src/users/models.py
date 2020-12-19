from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class ShopUser(models.Model):
    user = models.ForeignKey(User, default=1, null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=300,null=True)
    last_name = models.CharField(max_length=300,null=True)
    phone = models.CharField(max_length=150,null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    password = models.CharField(max_length=150,null=True)

    def __str__(self):
        return str(self.user.id)
from django_registration.forms import RegistrationForm
from users.models import ShopUser

class ShopUserForm(RegistrationForm):

    class Meta(RegistrationForm):
        model = ShopUser
        fields = '__all__'
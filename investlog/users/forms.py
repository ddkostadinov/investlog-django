from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email',]
        error_messages = {
            "username": {
                    "required": "Please enter a value!",
                    "max_length": "Max characters exceeded!"
            },
            "email": {
                "required": "Please enter a value!",
                "max_length": "Max characters exceeded!"
            },
            "password": {
                "required": "Please enter a value!",
                "max_length": "Max characters exceeded!"
            },
        }
            
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        error_messages = {
            "email": {
                "required": "Please enter a value!",
                "max_length": "Max characters exceeded!"
            },
            "password": {
                "required": "Please enter a value!",
                "max_length": "Max characters exceeded!"
            },
        }
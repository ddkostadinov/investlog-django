from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['email'].required = True
        
    class Meta:
        model = User
        fields = ['username', 'email',]
            
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
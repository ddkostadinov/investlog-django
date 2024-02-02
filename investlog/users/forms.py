from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
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
        
class UsernameChangeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        
    new_username = forms.CharField(label='New Username', max_length=150)

    class Meta:
        model = User
        fields = ['username']
        
    def clean_new_username(self):
        new_username = self.cleaned_data.get('new_username')
        current_username = self.cleaned_data.get('username')
        
        if User.objects.filter(username=new_username).exists() or current_username != self.instance.username:
            raise forms.ValidationError('This username is already taken. Please choose a different one.')
        return new_username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['new_username']

        if commit:
            user.save()
        return user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
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
    
class PasswordChangeForm(PasswordChangeForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['password'].help_text = None
        
    # new_password = forms.CharField(label='New Password', max_length=150)

    class Meta:
        model = User
        fields = ['__all__']
        
    # def clean_new_password(self):
    #     new_password = self.cleaned_data.get('new_password')
    #     current_password = self.cleaned_data.get('password')
        
    #     if User.objects.filter(password=new_password).exists() or current_password != self.instance.password:
    #         raise forms.ValidationError('This password is already taken. Please choose a different one.')
    #     return new_password

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.password = self.cleaned_data['new_password']

    #     if commit:
    #         user.save()
    #     return user
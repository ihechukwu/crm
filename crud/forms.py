from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AbstractUser
from .models import Record
from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput

# -register/create user
class UserRegisterForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1','password2']
        
# login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
# create a record
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','city','state','country']
        
        
# update record
class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        model = Record
        fields = ['first_name','last_name','email','phone','city','state','country']
    
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField
    #constituancy = forms.CharField(max_length=200)
    #last_name = forms.CharField

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1', 'password2']
class RegisterForm(forms.ModelForm):
    #email = forms.EmailField
    constituancy = forms.CharField(max_length=200)
    #last_name = forms.CharField

    class Meta:
        model = Profile
        fields = ['phone_num', 'voters_card_num','constituancy','image']

class UserUpdateForm(forms.ModelForm):
   # email = forms.EmailField

    # FirstName = forms.CharField(max_length=50)
    # LastName = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields =['phone_num','voters_card_num','constituancy','image']
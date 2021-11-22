from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm, UsernameField
from django.core import validators

def validete_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

class UserCreation(UserCreationForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"placeholder":"Password",'autocomplete':'new-password','id':''}),error_messages={"required":"Please enter password"},)
    password2 = forms.CharField(label="Repeat your password",widget= forms.PasswordInput(attrs={"placeholder":"Repeat your password",'autocomplete':'new-password','id':''}),help_text="Make sure your password contains 'small letter','capital letter','numbers' and 'symbols'",error_messages={"required":"Re-Enter password field cannot be empty"})
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"placeholder":"Username","id":"username",'class':'','id':'name'}),validators=[validete_username])
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True,'id':'fname'}),error_messages={"required":"First name cannot be empty"})
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name","required":True,'id':'lname'}),error_messages={"required":"Last name cannot be empty"})
    email = forms.CharField(widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Email",'autocomplete':'username','id':'email'}))
    class  Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']
        

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"placeholder":"Username",'class':'','id':'your_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password",'autocomplete':'current-password','class':'','id':'your_pass'}))    
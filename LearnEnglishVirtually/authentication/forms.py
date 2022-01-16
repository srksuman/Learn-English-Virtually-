from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm, UsernameField, UserChangeForm
from django.core import validators

def validate_username(value):
    if len(value)<=2:
        raise forms.ValidationError(f"Your username cannot be of {len(value)}  word")

def validate_email(value):
    print('Email error check')
    email = User.objects.filter(email=value)
    if email:
        raise forms.ValidationError(f"This '{value}' email already exists!!!!!!! ")


class UserCreation(UserCreationForm):
    password1 = forms.CharField(label="Password", widget = forms.PasswordInput(attrs={"placeholder":"Password",'autocomplete':'new-password','id':''}),error_messages={"required":"Please enter password"},)
    password2 = forms.CharField(label="Repeat your password",widget= forms.PasswordInput(attrs={"placeholder":"Repeat your password",'autocomplete':'new-password','id':''}),help_text="Make sure your password contains 'small letter','capital letter','numbers' and 'symbols'",error_messages={"required":"Re-Enter password field cannot be empty"})
    username = forms.CharField(label="username",widget=forms.TextInput(attrs={"placeholder":"Username","id":"username",'class':'','id':'name'}),validators=[validate_username])
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First Name","required":True,'id':'fname'}),error_messages={"required":"First name cannot be empty"})
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last Name","required":True,'id':'lname'}),error_messages={"required":"Last name cannot be empty"})
    email = forms.CharField(widget=forms.EmailInput(attrs={"required":True,"Placeholder":"Email",'autocomplete':'username','id':'email'}),validators=[validate_email])
    class  Meta:
        model = User
        fields =['username','email','first_name','last_name','password1','password2']
        

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"placeholder":"Username",'class':'','id':'your_name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"password",'autocomplete':'current-password','class':'','id':'your_pass'}))    


class VerifyForm(forms.Form):
    otp = forms.CharField(label='OTP',max_length=70,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'One Time Password','required':True}),error_messages={'required':'One Time Password is Required'})

class ChangePasswordUserForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'','placeholder':'old password'}),error_messages={"required":"Old Password Field is required"})
    new_password1 =forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'','placeholder':'new password'}),error_messages={"required":"New Password Field is  required"}) 
    new_password2 =forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'','placeholder':'confirm password'}),error_messages={"required":"Confirm Field is  required"}) 
    
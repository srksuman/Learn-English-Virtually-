from django import forms
from django.core import validators

# def validate_email(value):



class ContactForm(forms.Form):
        message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control valid',"onfocus":"this.placeholder = ''","onblur":"this.placeholder = 'Enter Message'" ,"placeholder":" Enter Message","required":True,"name":"message","id":"message"}),error_messages={"required":"um...yea, you have to write something to send this form."})
        name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control valid","name":"name","id":"name","type":"text","onfocus":"this.placeholder = ''","onblur":"this.placeholder = 'Enter your name'","required":True,"placeholder":"Enter your name"}),error_messages={"required":"come on, you have a name, don't you?"})
        email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={"class":"form-control valid","name":"email","id":"email","type":"email","onfocus":"this.placeholder = ''","onblur":"this.placeholder = 'Enter your email'","required":True,"placeholder":"Email"}),error_messages={"required":"no email, no message"})
        Subject = forms.CharField(max_length=50,widget=forms.TextInput(attrs={"class":"form-control","name":"subject","id":"subject","type":"text","onfocus":"this.placeholder = ''","onblur":"this.placeholder = 'Enter subject'","required":True,"placeholder":"Enter subject"}),error_messages={"required":"come on, you have a subject, don't you?"})
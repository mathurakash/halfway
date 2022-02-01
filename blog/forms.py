from dataclasses import field
from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.admin.widgets import AdminDateWidget

from .models import Post



class SignUpForm(UserCreationForm):
    password1=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label="Confirm Password(again)",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.TextInput(attrs={'class':'form-control'}),
                
                }



class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_("Passwood"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','desc','post_date']
        labels={'title':'Title','desc':'Description','post_date':'Date'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                'desc':forms.Textarea(attrs={'class':'form-control'}),
                'post_date':forms.TextInput(attrs={'class':'form-control','PlaceHolder':'yyyy-mm-dd'}),
                }









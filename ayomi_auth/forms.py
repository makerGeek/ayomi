from django import forms
from django.contrib.auth.forms import UserCreationForm



class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="prenom")
    last_name = forms.CharField(max_length=50, label="nom")
    email = forms.EmailField()

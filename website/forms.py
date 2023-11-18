from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(Label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email Adress'})
	first_name = forms.CharField(Label="", max_length="50", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(Label="", max_length="50", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Last Name'})
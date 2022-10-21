from cProfile import label
from dataclasses import field, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm  
from .models import *
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question_Model
        fields = "__all__"

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
# import GeeksModel from models.py
from .models import LeaveData


class SignupForm(UserCreationForm):
    role = forms.CharField(max_length=50, label="Role (Employee or Manager)")
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','role']

# create a ModelForm
class LeaveDataForm(ModelForm):
    # specify the name of model to use
    class Meta:
        model = LeaveData
        #fields = "__all__"
        exclude = ('leave_status',)

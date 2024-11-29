from django import forms
from django.contrib.auth.models import User
from .models import Details
from .models import Marks

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['name', 'age', 'phone', 'address']

class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['maths', 'english', 'science']

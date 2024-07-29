#making forms in tweets
from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']


#making new form -> user registration form
class UserRegistrationForm(UserCreationForm):
    emails = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
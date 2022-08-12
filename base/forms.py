from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'username', 'password1', 'password2']


class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'avatar', 'bio']

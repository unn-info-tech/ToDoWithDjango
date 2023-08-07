from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class sozlangUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#-------------------------------------------------------------------

class sozlangUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class changeUsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']

class changeEmailForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email']
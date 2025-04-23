from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    """Форма регистрации с выбором роли"""
    role = forms.ChoiceField(choices=CustomUser.ROLES)
    phone = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'role', 'phone')

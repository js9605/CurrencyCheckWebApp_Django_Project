from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserCurrencies

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class AddUserCurrencyForm(forms.ModelForm):
    class Meta:
        model = UserCurrencies
        fields = ['currency_shortcut']


class CurrencyLimitForm(forms.ModelForm):
    class Meta:
        model = UserCurrencies
        fields = ['user_email', 'upper_limit', 'lower_limit']
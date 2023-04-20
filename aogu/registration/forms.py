from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(UserRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()

            return user
        

from django import forms

class ChangeLoginForm(forms.Form):
    current_login = forms.CharField(max_length=150)
    new_login = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from . import views
from .models import FilaUserManager
from django.contrib.auth import authenticate

class CustromUser(forms.Form):

    first_name = forms.CharField(label='Introdu Prenumele',min_length=1,max_length=20)
    last_name = forms.CharField(label='Introdu Nuemele de familie', min_length=4 , max_length=20)
    confirm_email = forms.EmailField(label='introdu Confirmarea_emailului')
    email = forms.EmailField(label='Introdu Emailu')
    confirm_password = forms.CharField(label='Introdu Confirmarea Parolei',widget=forms.PasswordInput)
    password = forms.CharField(label='Introdu Parola',widget=forms.PasswordInput)

    class Meta:

        fields =(
            'first_name',
            'last_name',
            'email',
            'confirm_email',
            'password',
            'confirm_password'
        )


    def clean_first_name(self):

        first_name = self.cleaned_data['first_name']

        return first_name

    def clean_last_name(self):

        last_name = self.cleaned_data['last_name']

        return last_name

    def clean_email(self):

        confirm_email = self.cleaned_data['confirm_email']
        email = self.cleaned_data['email']

        if email and confirm_email and email != confirm_email:
            raise ValidationError("emails don't match")

        user = User.objects.filter(email=email)
        if user.count():
            raise ValidationError('email already exists')

        return confirm_email

    def clean_password(self):

        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords don't match")

        return confirm_password

    def save(self,commit = True):

        user = User.objects.create_user(
            self.cleaned_data['first_name'] + ' ' + self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
        )

        return user

"""class RegistrationForm(UserCreationForm):

    email = models.EmailField(required=True,validators=[validate_email],widget=forms.EmailInput(attrs={'placeholder':'Introduceti Emailul'}))

    class Meta:

        model = FilaUser

        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

    def save(self,commit = True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.email = self.cleaned_data('email')

        if commit:
            print('saving now')
            user.save()

        return user

class CustomAuthForm(AuthenticationForm):

    remember_me = forms.BooleanField(
                    label='Remember Me',
                    required=False,
                    widget=forms.CheckboxInput())

    def clean(self):

        super().clean()

        remember = self.cleaned_data.get('remember_me')
        if not remember:
            self.request.session.set_expiry(0)

        return remember
"""
"""

class UserForm(forms.ModelForm):
    parola = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(
        required=True,
        validators=[validate_email],
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Your Email'
        }))

    class Meta:
        model = User

        fields = (
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        Nume = self.cleaned_data.get('Nume')
        Prenume = self.cleaned_data.get('Prenume')

        email = self.cleaned_data('Email')
        confirm_email = self.cleaned_data('Confirmare_Email')

        parola = self.cleaned_data('Parola')
        confirmare_parola = self.cleaned_data('Confirmare_Parola')

        if commit:
            print('saving now')

            user.set_password(parola)
            user.save()

        user = authenticate(email=email, parola=parola, Nume=Nume)

        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
"""
"""remember_me = forms.BooleanField(label='Remember Me', required=False, widget=forms.CheckboxInput())

def clean(self):
    super().clean()
    remember = self.cleaned_data.get('remember_me')
    if not remember:
        self.request.session.set_expiry(0)
    return remember"""

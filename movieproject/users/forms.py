from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Movie


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password don't match ")
        return cd['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('date_of_birth', 'photo')


class MovieForm(forms.Form):
    movie_id = forms.IntegerField()

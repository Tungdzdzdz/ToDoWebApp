from django.contrib.auth.models import User
from django import forms

from user_profile.models import Profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=125)

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'dob', 'avatar']

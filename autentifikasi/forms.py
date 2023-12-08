from django.forms import ModelForm
from django import forms
from user_profile.models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "description"]

class CustomUserCreationForm(UserCreationForm):
    is_staff = forms.BooleanField(
        label="Register as staff",
        required=False,
        initial=False,
        help_text="Check this box if the user is a staff member."
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('is_staff', )
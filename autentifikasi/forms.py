from django.forms import ModelForm
from user_profile.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "description"]
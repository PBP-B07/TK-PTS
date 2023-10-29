from django import forms
from django.forms import ModelForm
from forum.models import Forum

class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["subject", "description"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
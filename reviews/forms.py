from django import forms
from django.forms import ModelForm
from reviews.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['star', 'description']
        widgets = {
            "star": forms.TextInput(attrs={"type": "range", "class": "form-control", "min": "0", "max": "5", "value": "0"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
        }
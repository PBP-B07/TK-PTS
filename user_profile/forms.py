from django.forms import ModelForm
from reviews.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["star", "description"]
from django.forms import ModelForm
from reviews.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["star", "description"]
    
    def __init__(self, args, **kwargs): 
        super().__init__(args, **kwargs)
        self.fields['description'].widget.attrs.update({ 
            'type' : 'text-area',
            'class': 'form-control', 
            'id':'review_description', 
            'name':'review_description',
        })
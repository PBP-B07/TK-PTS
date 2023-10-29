from django import forms
from django.forms import ModelForm
from homepage.models import BookEvent

class HomepageForm(ModelForm):
    class Meta:
        model = BookEvent
        fields = [ "title", "description"]
        
        def __init__(self, args, **kwargs): 
            super().__init__(args, **kwargs)
            self.fields['title'].widget.attrs.update({ 
                'type' : 'text',
                'class': 'form-control', 
            })
            
            self.fields['description'].widget.attrs.update({ 
                'type' : 'text-area',
                'class': 'form-control', 
            })
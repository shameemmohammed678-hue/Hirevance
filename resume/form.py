from django import forms
from .models import Resume

class Resumeform(forms.ModelForm):
    
    class Meta:
        model = Resume
        fields = ['resume']

        widgets = {
            'resume':forms.FileInput(attrs={
                'accept':'.pdf,.doc,.docx'
            }),
        } 
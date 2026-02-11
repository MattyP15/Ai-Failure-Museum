##thank god for djangos modelform 


from django import forms
from .models import artefact

class ArtefactForm(forms.ModelForm):
    class Meta:
        model = artefact
        fields = ['title', 'file']
        
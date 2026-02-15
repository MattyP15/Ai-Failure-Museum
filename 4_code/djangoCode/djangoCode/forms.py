##thank god for djangos modelform 


from django import forms
from .models import Artefact

class ArtefactForm(forms.ModelForm):
    class Meta:
        model = Artefact
        fields = ['title', 'file']
        
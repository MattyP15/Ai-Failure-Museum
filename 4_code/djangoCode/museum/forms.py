from django import forms
from .models import Exhibit, Quiz

class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['title', 'category', 'domain','description','deployment_context', 'intended_use', 'system_type', 'what_went_wrong','data_issues', 'recommendations', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'deployment_context': forms.Textarea(attrs={'rows': 3}),
            'intended_use': forms.Textarea(attrs={'rows': 3}),
            'what_went_wrong': forms.Textarea(attrs={'rows': 3}),
            'data_issues': forms.Textarea(attrs={'rows': 3}),
            'recommendations': forms.Textarea(attrs={'rows': 3}),
        }


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['exhibit', 'title', 'description', 'is_active', 'points_for_completion']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }
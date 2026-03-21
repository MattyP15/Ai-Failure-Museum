from django import forms
from .models import Exhibit, Quiz, Comment, UserSubmission

class ExhibitForm(forms.ModelForm):
    class Meta:
        model = Exhibit
        fields = ['title', 'category', 'failure_type', 'deployment_context',
        'intended_use', 'artefact1', 'system_type', 'inputs_assumptions',
        'outputs_to_users', 'artefact2', 'what_went_wrong', 'how_detected',
        'who_affected', 'artefact3', 'data_issues', 'design_choices',
        'org_governance_issues', 'artefact4', 'recommendations',
        'warnings', 'artefact5', 'description', 'is_archived',]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'deployment_context': forms.Textarea(attrs={'rows': 3}),
            'intended_use': forms.Textarea(attrs={'rows': 3}),
            'what_went_wrong': forms.Textarea(attrs={'rows': 3}),
            'data_issues': forms.Textarea(attrs={'rows': 3}),
            'recommendations': forms.Textarea(attrs={'rows': 3}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Share your thoughts on this exhibit...'
            }),
        }
        labels = {'body': ''}


class UserSubmissionForm(forms.ModelForm):
    class Meta:
        model = UserSubmission
        fields = ['title', 'category', 'description', 'what_went_wrong',
                  'who_affected', 'source_url', 'artefact']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'what_went_wrong': forms.Textarea(attrs={'rows': 3}),
            'who_affected': forms.Textarea(attrs={'rows': 2}),
        }


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['exhibit', 'title', 'description', 'is_active', 'points_for_completion']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

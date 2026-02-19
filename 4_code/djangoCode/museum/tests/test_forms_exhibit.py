from django.test import TestCase
from museum.forms import ExhibitForm

class ExhibitFormTests(TestCase):
    def test_exhibit_form_missing_title_invalid(self):
        form_data = {
            "title": "",
            "category": "Test",
            "failure_type": "Test",
            "description": "desc",
            "deployment_context": "context",
            "intended_use": "use",
            "system_type": "type",
            "what_went_wrong": "wrong",
            "data_issues": "issues",
            "recommendations": "recs",
        }
        form = ExhibitForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
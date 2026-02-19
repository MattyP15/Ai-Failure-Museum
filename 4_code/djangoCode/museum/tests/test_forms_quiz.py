from django.test import TestCase
from museum.forms import QuizForm
from museum.models import Exhibit


class QuizFormTests(TestCase):

    def setUp(self):
        self.exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            description="Desc"
        )

    def test_quiz_form_invalid_without_title(self):
        form = QuizForm(data={
            "exhibit": self.exhibit.id,
            "title": "",
            "points_for_completion": 10,
        })
        self.assertFalse(form.is_valid())

    def test_quiz_form_valid(self):
        form = QuizForm(data={
            "exhibit": self.exhibit.id,
            "title": "Sample Quiz",
            "points_for_completion": 10,
        })
        self.assertTrue(form.is_valid())

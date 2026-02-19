import json

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from museum.models import Exhibit, Quiz, Question, AnswerOption, UserProfile


class ApiQuizSubmitTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

        self.exhibit = Exhibit.objects.create(title="Exhibit1", description="Desc")
        self.quiz = Quiz.objects.create(
            exhibit=self.exhibit,
            title="Quiz 1",
            is_active=True,
            points_for_completion=10,
        )

        self.q1 = Question.objects.create(
            quiz=self.quiz,
            prompt="choose 1",
            qtype=Question.MULTIPLE_CHOICE,
            order=1,
        )

        self.a = AnswerOption.objects.create(
            question=self.q1,
            text="A",
            is_correct=True,
            order=1,
        )

        AnswerOption.objects.create(
            question=self.q1,
            text="B",
            is_correct=False,
            order=2,
        )

    def test_api_quiz_submit(self):
        UserProfile.objects.update_or_create(user=self.user, defaults={"points": 0})
        url = reverse("api_quiz_submit", args=[self.quiz.id])

        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 400)

        resp = self.client.post(url, "bad", content_type="application/json")
        self.assertEqual(resp.status_code, 400)

        resp = self.client.post(
            url,
            data=json.dumps({"answers": "wrong"}),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 400)

        payload = {"answers": [{"question_id": self.q1.id, "option_id": self.a.id}]}
        resp = self.client.post(url, data=json.dumps(payload), content_type="application/json")

        self.assertEqual(resp.status_code, 200)

        data = resp.json()
        self.assertEqual(data["status"], "ok")
        self.assertEqual(data["points_awarded"], self.quiz.points_for_completion)
        self.assertEqual(data["total_points"], self.quiz.points_for_completion)

        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.points, self.quiz.points_for_completion)

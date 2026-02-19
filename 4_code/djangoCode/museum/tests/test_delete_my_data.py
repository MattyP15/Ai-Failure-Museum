from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from museum.models import Quiz, Exhibit, QuizAttempt, UserBadge, Badge


class DeleteMyDataTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_get_delete_my_data_page(self):
        url = reverse("delete_my_data")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_post_deletes_account_and_related_data(self):
        # Create related data that should be deleted
        exhibit = Exhibit.objects.create(title="Ex", description="Desc")
        quiz = Quiz.objects.create(exhibit=exhibit, title="Q1", description="", is_active=True, points_for_completion=10)

        attempt = QuizAttempt.objects.create(user=self.user, quiz=quiz)

        badge = Badge.objects.create(code="b1", name="Badge 1", points_threshold=0)
        UserBadge.objects.create(user=self.user, badge=badge)

        # Sanity checks (data exists before delete)
        User = get_user_model()
        self.assertTrue(User.objects.filter(id=self.user.id).exists())
        self.assertTrue(QuizAttempt.objects.filter(id=attempt.id).exists())
        self.assertTrue(UserBadge.objects.filter(user=self.user).exists())

        # Perform delete
        url = reverse("delete_my_data")
        resp = self.client.post(url)

        # Should redirect to "/"
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp["Location"], "/")

        # User should be deleted
        self.assertFalse(User.objects.filter(id=self.user.id).exists())

        # Related rows should be gone too
        self.assertEqual(QuizAttempt.objects.filter(user_id=self.user.id).count(), 0)
        self.assertEqual(UserBadge.objects.filter(user_id=self.user.id).count(), 0)

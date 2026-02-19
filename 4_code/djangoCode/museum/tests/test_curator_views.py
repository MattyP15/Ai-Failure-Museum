from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CuratorViewAccessTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")

    def test_non_curator_blocked_from_curator_dashboard(self):
        url = reverse("curator_dashboard")
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (302, 403), msg=f"Got {resp.status_code}")

    def test_non_curator_blocked_from_create_exhibit(self):
        url = reverse("create_exhibit")
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (302, 403), msg=f"Got {resp.status_code}")

    def test_non_curator_blocked_from_analytics_dashboard(self):
        url = reverse("analytics_dashboard")
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (302, 403), msg=f"Got {resp.status_code}")

    def test_non_curator_blocked_from_edit_exhibit(self):
        from museum.models import Exhibit

        exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            description="Short description",
        )

        url = reverse("edit_exhibit", args=[exhibit.id])
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (302, 403), msg=f"Got {resp.status_code}")

    def test_non_curator_blocked_from_delete_exhibit(self):
        from museum.models import Exhibit

        exhibit = Exhibit.objects.create(
            title="Test Exhibit",
            description="Short description",
        )

        url = reverse("delete_exhibit", args=[exhibit.id])
        resp = self.client.get(url)
        self.assertIn(resp.status_code, (302, 403), msg=f"Got {resp.status_code}")

from django.test import TestCase
from django.contrib.auth import get_user_model 


from museum.gamification import award_points 
from museum.models import UserProfile


class AwardPointsTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

    def test_award_points(self):
        total, newly = award_points(self.user, 10)

        # Total Points returned
        self.assertEqual(total, 10)
        # No badge awarded yet
        self.assertEqual(newly, [])
        # Check database correctly updated
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(profile.points, 10)


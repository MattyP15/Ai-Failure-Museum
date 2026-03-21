from django.test import TestCase 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from museum.rbac import is_curator 

class RBACTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser", 
            password="testpassword"
        )

    def test_regular_user_not_a_curator(self):
        self.assertFalse(is_curator(self.user))

    def test_staff_is_curator(self):
        self.user.is_staff = True
        self.user.save()
        self.assertTrue(is_curator(self.user))

    def test_curator_group_is_curator(self):
        curator = Group.objects.create(name="Curator")
        self.user.groups.add(curator)
        self.assertTrue(is_curator(self.user))

    def test_anonymous_is_not_a_curator(self):
        class imposter:
            is_authenticated = False
            is_staff = False

            @property
            def groups(self):
                return Group.objects.none()
            
        self.assertFalse(is_curator(imposter()))
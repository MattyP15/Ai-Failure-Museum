# Basic Test Suite for AI Failure Museum

This document provides basic tests you should create after completing the integration.

---

## 📁 Test File Structure

Create these test files in the `museum/` app:

```
museum/
├── tests/
│   ├── __init__.py
│   ├── test_models.py      # Test database models
│   ├── test_views.py       # Test view functions
│   ├── test_security.py    # Test authentication/authorization
│   └── test_rbac.py        # Test role-based access control
```

---

## 🧪 Test Files to Create

### 1. Create `museum/tests/__init__.py` (empty file)

This makes the `tests/` folder a Python package.

**Action:**
```bash
cd 4_code/djangoCode
mkdir museum/tests
touch museum/tests/__init__.py  # Mac/Linux
type nul > museum/tests\__init__.py  # Windows
```

---

### 2. Create `museum/tests/test_models.py`

Tests for your database models.

**Content to add:**

```python
from django.test import TestCase
from django.contrib.auth.models import User
from museum.models import (
    Artefact, UserProfile, Badge, UserBadge,
    Quiz, Question, AnswerOption, QuizAttempt, Response
)


class ArtefactModelTest(TestCase):
    """Test the Artefact model"""

    def setUp(self):
        """Create test data"""
        self.artefact = Artefact.objects.create(
            title="Test Artefact",
            domain="Testing",
            description="A test artefact for unit testing",
            is_archived=False
        )

    def test_artefact_creation(self):
        """Test creating an artefact"""
        self.assertEqual(self.artefact.title, "Test Artefact")
        self.assertEqual(self.artefact.domain, "Testing")
        self.assertFalse(self.artefact.is_archived)

    def test_artefact_str_method(self):
        """Test string representation"""
        self.assertEqual(str(self.artefact), "Test Artefact")

    def test_artefact_archive(self):
        """Test archiving an artefact"""
        self.artefact.is_archived = True
        self.artefact.save()

        updated = Artefact.objects.get(pk=self.artefact.pk)
        self.assertTrue(updated.is_archived)


class UserProfileModelTest(TestCase):
    """Test the UserProfile model"""

    def setUp(self):
        """Create test user"""
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_profile_autocreation(self):
        """Test that UserProfile is created automatically via signals"""
        # Profile should be auto-created by signal
        self.assertTrue(hasattr(self.user, 'userprofile'))
        self.assertEqual(self.user.userprofile.points, 0)

    def test_profile_points_update(self):
        """Test updating user points"""
        profile = UserProfile.objects.get(user=self.user)
        profile.points = 50
        profile.save()

        updated = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated.points, 50)


class BadgeModelTest(TestCase):
    """Test the Badge and UserBadge models"""

    def setUp(self):
        """Create test data"""
        self.badge = Badge.objects.create(
            code="test_badge",
            name="Test Badge",
            description="A badge for testing",
            points_threshold=100
        )
        self.user = User.objects.create_user(
            username='badgeuser',
            password='testpass123'
        )

    def test_badge_creation(self):
        """Test creating a badge"""
        self.assertEqual(self.badge.code, "test_badge")
        self.assertEqual(self.badge.points_threshold, 100)

    def test_user_badge_award(self):
        """Test awarding a badge to a user"""
        user_badge = UserBadge.objects.create(
            user=self.user,
            badge=self.badge
        )

        self.assertEqual(user_badge.user, self.user)
        self.assertEqual(user_badge.badge, self.badge)
        self.assertIsNotNone(user_badge.awarded_at)


class QuizModelTest(TestCase):
    """Test Quiz-related models"""

    def setUp(self):
        """Create test quiz"""
        self.quiz = Quiz.objects.create(
            title="Test Quiz",
            description="A test quiz",
            is_active=True,
            points_for_completion=10
        )
        self.question = Question.objects.create(
            quiz=self.quiz,
            prompt="What is AI?",
            qtype=Question.TEXT,
            order=0
        )

    def test_quiz_creation(self):
        """Test creating a quiz"""
        self.assertEqual(self.quiz.title, "Test Quiz")
        self.assertTrue(self.quiz.is_active)
        self.assertEqual(self.quiz.points_for_completion, 10)

    def test_question_creation(self):
        """Test creating a question"""
        self.assertEqual(self.question.prompt, "What is AI?")
        self.assertEqual(self.question.qtype, Question.TEXT)
        self.assertEqual(self.question.quiz, self.quiz)

    def test_question_ordering(self):
        """Test that questions are ordered correctly"""
        q2 = Question.objects.create(
            quiz=self.quiz,
            prompt="Question 2",
            qtype=Question.TEXT,
            order=1
        )

        questions = self.quiz.questions.all()
        self.assertEqual(questions[0], self.question)
        self.assertEqual(questions[1], q2)
```

---

### 3. Create `museum/tests/test_security.py`

Tests for authentication and authorization.

**Content to add:**

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from django.urls import reverse


class SecurityTest(TestCase):
    """Test authentication and authorization"""

    def setUp(self):
        """Create test users and client"""
        self.client = Client()

        # Create Curator group
        self.curator_group = Group.objects.create(name="Curator")

        # Create regular user
        self.regular_user = User.objects.create_user(
            username='regular',
            password='regularpass123'
        )

        # Create curator user
        self.curator_user = User.objects.create_user(
            username='curator',
            password='curatorpass123'
        )
        self.curator_user.groups.add(self.curator_group)

        # Create admin user
        self.admin_user = User.objects.create_user(
            username='admin',
            password='adminpass123',
            is_staff=True
        )

    def test_curator_dashboard_requires_login(self):
        """Test that curator dashboard redirects if not logged in"""
        response = self.client.get('/curator/dashboard/')

        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_regular_user_cannot_access_curator_dashboard(self):
        """Test that regular users can't access curator features"""
        self.client.login(username='regular', password='regularpass123')
        response = self.client.get('/curator/dashboard/')

        # Should redirect (not authorized)
        self.assertEqual(response.status_code, 302)

    def test_curator_can_access_dashboard(self):
        """Test that curators can access curator dashboard"""
        self.client.login(username='curator', password='curatorpass123')
        response = self.client.get('/curator/dashboard/')

        # Should be successful
        self.assertEqual(response.status_code, 200)

    def test_admin_can_access_curator_dashboard(self):
        """Test that admin users have curator access"""
        self.client.login(username='admin', password='adminpass123')
        response = self.client.get('/curator/dashboard/')

        # Should be successful (staff users are curators)
        self.assertEqual(response.status_code, 200)

    def test_create_artefact_requires_authentication(self):
        """Test that creating artefacts requires login"""
        response = self.client.get('/curator/create/')

        # Should redirect to login
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_delete_artefact_requires_curator_role(self):
        """Test that deleting artefacts requires curator role"""
        # Try as regular user
        self.client.login(username='regular', password='regularpass123')
        response = self.client.post('/curator/delete/1/')

        # Should redirect (not authorized)
        self.assertEqual(response.status_code, 302)


class RBACTest(TestCase):
    """Test role-based access control functions"""

    def setUp(self):
        """Create test users"""
        self.curator_group = Group.objects.create(name="Curator")

        self.regular_user = User.objects.create_user(
            username='regular',
            password='pass123'
        )

        self.curator_user = User.objects.create_user(
            username='curator',
            password='pass123'
        )
        self.curator_user.groups.add(self.curator_group)

        self.staff_user = User.objects.create_user(
            username='staff',
            password='pass123',
            is_staff=True
        )

    def test_is_curator_for_regular_user(self):
        """Test that regular users are not curators"""
        from museum.rbac import is_curator
        self.assertFalse(is_curator(self.regular_user))

    def test_is_curator_for_curator_user(self):
        """Test that users in Curator group are curators"""
        from museum.rbac import is_curator
        self.assertTrue(is_curator(self.curator_user))

    def test_is_curator_for_staff_user(self):
        """Test that staff users are curators"""
        from museum.rbac import is_curator
        self.assertTrue(is_curator(self.staff_user))

    def test_is_curator_for_unauthenticated(self):
        """Test that unauthenticated users are not curators"""
        from museum.rbac import is_curator
        from django.contrib.auth.models import AnonymousUser

        anonymous = AnonymousUser()
        self.assertFalse(is_curator(anonymous))
```

---

### 4. Create `museum/tests/test_views.py`

Tests for view functions.

**Content to add:**

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User, Group
from museum.models import Artefact, Quiz, Question


class ViewTest(TestCase):
    """Test view functions"""

    def setUp(self):
        """Create test data"""
        self.client = Client()

        # Create curator user
        curator_group = Group.objects.create(name="Curator")
        self.curator = User.objects.create_user(
            username='curator',
            password='curatorpass'
        )
        self.curator.groups.add(curator_group)

        # Create test artefact
        self.artefact = Artefact.objects.create(
            title="Test Exhibit",
            domain="Testing",
            description="Test description",
            is_archived=False
        )

    def test_homepage_accessible(self):
        """Test that homepage loads"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_curator_dashboard_shows_artefacts(self):
        """Test that curator dashboard displays artefacts"""
        self.client.login(username='curator', password='curatorpass')
        response = self.client.get('/curator/dashboard/')

        self.assertEqual(response.status_code, 200)
        self.assertIn('active_artefacts', response.context)
        self.assertIn('archived_artefacts', response.context)

    def test_archive_artefact(self):
        """Test archiving an artefact"""
        self.client.login(username='curator', password='curatorpass')

        # Archive the artefact
        response = self.client.get(f'/curator/archive/{self.artefact.pk}/')

        # Should redirect back to dashboard
        self.assertEqual(response.status_code, 302)

        # Check artefact is archived
        self.artefact.refresh_from_db()
        self.assertTrue(self.artefact.is_archived)

    def test_delete_artefact(self):
        """Test deleting an artefact"""
        self.client.login(username='curator', password='curatorpass')
        artefact_pk = self.artefact.pk

        # Delete the artefact
        response = self.client.get(f'/curator/delete/{artefact_pk}/')

        # Should redirect back to dashboard
        self.assertEqual(response.status_code, 302)

        # Check artefact is deleted
        self.assertFalse(Artefact.objects.filter(pk=artefact_pk).exists())


class QuizAPITest(TestCase):
    """Test quiz API endpoints"""

    def setUp(self):
        """Create test quiz"""
        self.client = Client()

        self.user = User.objects.create_user(
            username='quizuser',
            password='quizpass'
        )

        self.quiz = Quiz.objects.create(
            title="Test Quiz",
            description="Test description",
            is_active=True,
            points_for_completion=10
        )

        self.question = Question.objects.create(
            quiz=self.quiz,
            prompt="Test question?",
            qtype=Question.TEXT,
            order=0
        )

    def test_api_quizzes_list(self):
        """Test fetching quiz list"""
        response = self.client.get('/api/quizzes/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('quizzes', data)
        self.assertEqual(len(data['quizzes']), 1)
        self.assertEqual(data['quizzes'][0]['title'], "Test Quiz")

    def test_api_quiz_detail(self):
        """Test fetching single quiz details"""
        response = self.client.get(f'/api/quizzes/{self.quiz.id}/')

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data['title'], "Test Quiz")
        self.assertEqual(len(data['questions']), 1)

    def test_quiz_submit_requires_login(self):
        """Test that quiz submission requires login"""
        response = self.client.post(
            f'/api/quizzes/{self.quiz.id}/submit/',
            data='{"answers": []}',
            content_type='application/json'
        )

        # Should redirect to login (302) or return 403
        self.assertIn(response.status_code, [302, 403])
```

---

## 🏃 Running the Tests

### Run All Tests

```bash
cd 4_code/djangoCode
python manage.py test
```

### Run Specific Test File

```bash
# Test only models
python manage.py test museum.tests.test_models

# Test only security
python manage.py test museum.tests.test_security

# Test only views
python manage.py test museum.tests.test_views
```

### Run Specific Test Class

```bash
python manage.py test museum.tests.test_models.ArtefactModelTest
```

### Run Specific Test Method

```bash
python manage.py test museum.tests.test_models.ArtefactModelTest.test_artefact_creation
```

### Run with Verbosity

```bash
# Verbose output
python manage.py test -v 2

# Very verbose
python manage.py test -v 3
```

### Run with Coverage (Optional)

First install coverage:
```bash
pip install coverage
```

Then run:
```bash
coverage run --source='museum' manage.py test museum
coverage report
coverage html  # Creates htmlcov/index.html
```

---

## ✅ Expected Test Results

After integration, you should see output like:

```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....................
----------------------------------------------------------------------
Ran 20 tests in 2.456s

OK
Destroying test database for alias 'default'...
```

If tests fail, read the error messages carefully - they'll tell you:
- Which test failed
- What was expected vs. what actually happened
- Line numbers for debugging

---

## 🐛 Common Test Failures

### "No such table: museum_artefact"

**Problem:** Migrations not applied to test database

**Fix:** Tests create their own temporary database, but need your models. Make sure:
```bash
python manage.py makemigrations
```

### "RelatedObjectDoesNotExist: User has no userprofile"

**Problem:** Signal not firing to create UserProfile

**Fix:** Make sure `museum/apps.py` has:
```python
class MuseumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'museum'

    def ready(self):
        import museum.signals  # Import signals
```

And in `museum/__init__.py`:
```python
default_app_config = 'museum.apps.MuseumConfig'
```

### "Template does not exist"

**Problem:** Test trying to render template that doesn't exist yet

**Fix:** Either:
1. Create the template
2. Or modify test to check response.status_code only

---

## 📝 Test Checklist

After integration, verify these tests pass:

**Models:**
- [ ] Artefact creation
- [ ] Artefact archiving
- [ ] UserProfile auto-creation
- [ ] Badge creation
- [ ] Quiz and Question creation

**Security:**
- [ ] Curator dashboard requires login
- [ ] Regular users can't access curator tools
- [ ] Curators can access curator tools
- [ ] Staff users have curator access

**Views:**
- [ ] Homepage loads
- [ ] Curator dashboard shows artefacts
- [ ] Archive artefact works
- [ ] Delete artefact works
- [ ] Quiz API returns data

**RBAC:**
- [ ] is_curator() works for curator group members
- [ ] is_curator() works for staff users
- [ ] is_curator() returns False for regular users

---

## 🎯 Next Steps

1. **Create the test files** as shown above
2. **Run the tests** to see what fails
3. **Fix failing tests** by implementing missing features
4. **Add more tests** as you add features

**Testing best practices:**
- Write tests BEFORE implementing features (TDD)
- Test both success and failure cases
- Test edge cases (empty data, invalid input)
- Keep tests independent (don't rely on test order)
- Use descriptive test names

---

## 📚 Resources

- [Django Testing Documentation](https://docs.djangoproject.com/en/6.0/topics/testing/)
- [Django TestCase API](https://docs.djangoproject.com/en/6.0/topics/testing/tools/)
- [Django Client API](https://docs.djangoproject.com/en/6.0/topics/testing/tools/#the-test-client)


# AI Failure Museum - Integration Action Plan
## Step-by-Step Guide to Fix Structure & Security

**Branch:** Curator-Security-Model-MERGE
**Priority:** Structure → Security → Testing
**Approach:** Guided manual fixes (you'll do the work, I'll explain each step)

---

## 🎯 Goals

1. **Structure**: Move all files to correct Django locations
2. **Security**: Add authentication to curator tools
3. **Integration**: Merge the two curator dashboards
4. **Testing**: Get the app running and working

---

## 📋 Prerequisites - Fix Your Environment First

### Step 0: Fix Django Installation

You have two `.venv` folders and Django isn't installed. Here's what to do:

**Option A: Use root .venv (RECOMMENDED)**
```bash
# Go to project root
cd /Users/Randi/Documents/GitHub/Ai-Failure-Museum

# Make sure root .venv is activated
source .venv/bin/activate

# Install requirements
pip install -r 4_code/requirements.txt

# Verify Django is installed
python -c "import django; print(django.get_version())"
# Should print: 6.0.2

# Now you can run the server
cd 4_code/djangoCode
python manage.py runserver
```

**Option B: Use djangoCode/.venv**
```bash
# Go to djangoCode
cd /Users/Randi/Documents/GitHub/Ai-Failure-Museum/4_code/djangoCode

# Activate the local venv
source .venv/bin/activate

# Install requirements
pip install -r ../requirements.txt

# Verify
python -c "import django; print(django.get_version())"

# Run server
python manage.py runserver
```

**My Recommendation:** Use Option A (root .venv) because your requirements.txt is in `4_code/`, making it the logical place for the venv.

---

## 🔧 Phase 1: Clean Up & Prepare (15 minutes)

### Step 1.1: Backup Current State

Before making any changes, create a backup:

```bash
# Make sure you're on your merge branch
git branch --show-current
# Should show: Curator-Security-Model-MERGE

# Commit any uncommitted work
git add .
git commit -m "Pre-integration backup: all three branches merged"

# Create a backup branch (just in case)
git branch backup-before-integration

# Optional: Push to remote
git push origin Curator-Security-Model-MERGE
git push origin backup-before-integration
```

### Step 1.2: Understand Current State

Check what's in your database:
```bash
cd 4_code/djangoCode

# Check if database exists and what tables are there
python manage.py showmigrations

# This will show which migrations have been applied
```

**Expected output:** You should see migrations for both `djangoCode` and `museum` apps.

---

## 🏗️ Phase 2: File Reorganization (30-45 minutes)

We'll move files from `djangoCode/djangoCode/` to `museum/` where they belong.

### Step 2.1: Move Artefact Model

**Current location:** `djangoCode/djangoCode/models.py`
**New location:** `djangoCode/museum/models.py`

**Action:**
1. Open `djangoCode/djangoCode/models.py`
2. **Copy** (don't delete yet) the Artefact class:
   ```python
   class Artefact(models.Model):
       title = models.CharField(max_length=200)
       domain = models.CharField(max_length=100)  # NOTE: Fix typo later
       description = models.TextField()
       is_archived = models.BooleanField(default=False)
       file = models.FileField(upload_to='artefacts/')
       uploaded_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.title
   ```

3. Open `djangoCode/museum/models.py`
4. **Add to the END** of the file (after all existing models):
   ```python
   # Artifact model (moved from djangoCode.models)
   class Artefact(models.Model):
       title = models.CharField(max_length=200)
       domain = models.CharField(max_length=100)  # FIXED TYPO: was "domian"
       description = models.TextField()
       is_archived = models.BooleanField(default=False)
       file = models.FileField(upload_to='artefacts/')
       uploaded_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return self.title
   ```

5. **Save** `museum/models.py`
6. **DO NOT delete** `djangoCode/models.py` yet - we'll handle this later

### Step 2.2: Create museum/forms.py

**Action:**
1. Create new file: `djangoCode/museum/forms.py`
2. Copy content from `djangoCode/djangoCode/forms.py` but fix the import:
   ```python
   from django import forms
   from .models import Artefact  # Changed from djangoCode.models

   class ArtefactForm(forms.ModelForm):
       class Meta:
           model = Artefact
           fields = ['title', 'domain', 'description', 'file']  # Added domain, description
   ```

3. **Save** the file

### Step 2.3: Merge Curator Views into museum/views.py

This is the trickiest part - we need to merge TWO curator_dashboard functions.

**Current state:**
- `djangoCode/views.py` has: homepage, category, login, curator tools (NO security)
- `museum/views.py` has: security-aware views, quiz APIs

**Action:**

1. Open `djangoCode/museum/views.py`

2. **Add these imports at the top:**
   ```python
   from django.shortcuts import render, redirect, get_object_or_404
   from django.contrib import messages
   from django.contrib.auth.decorators import login_required

   from .models import Artefact  # ADD THIS
   from .forms import ArtefactForm  # ADD THIS
   from .rbac import is_curator
   ```

3. **Find the existing curator_dashboard function** (around line 39)

4. **Replace it** with this merged version:
   ```python
   @login_required
   def curator_dashboard(request):
       """
       Merged curator dashboard showing artefact management.
       Requires user to be logged in and have curator role.
       """
       if not is_curator(request.user):
           messages.error(request, "You need curator permissions to access this page.")
           return redirect('/login/?next=/curator/dashboard/')

       # Get artefacts for display
       active_artefacts = Artefact.objects.filter(is_archived=False)
       archived_artefacts = Artefact.objects.filter(is_archived=True)

       return render(request, 'curator/dashboard.html', {
           'active_artefacts': active_artefacts,
           'archived_artefacts': archived_artefacts
       })
   ```

5. **Add all the curator tool functions** from `djangoCode/views.py` to `museum/views.py`:

   ```python
   @login_required
   def create_artefact(request):
       """Create a new artefact. Curators only."""
       if not is_curator(request.user):
           return redirect('/login/?next=/curator/')

       if request.method == 'POST':
           form = ArtefactForm(request.POST, request.FILES)
           if form.is_valid():
               artefact = form.save()
               messages.success(request, f'Artefact "{artefact.title}" created successfully!')
               return redirect('curator_dashboard')
       else:
           form = ArtefactForm()

       return render(request, 'curator/create_artefact.html', {'form': form})


   @login_required
   def delete_artefact(request, pk):
       """Delete an artefact permanently. Curators only."""
       if not is_curator(request.user):
           return redirect('/login/?next=/curator/')

       try:
           artefact = get_object_or_404(Artefact, pk=pk)
           artefact_title = artefact.title
           artefact.delete()
           messages.success(request, f'Artefact "{artefact_title}" deleted successfully.')
       except Exception as e:
           messages.error(request, f'Error deleting artefact: {e}')

       return redirect('curator_dashboard')


   @login_required
   def archive_artefact(request, pk):
       """Archive an artefact (hide from visitors). Curators only."""
       if not is_curator(request.user):
           return redirect('/login/?next=/curator/')

       try:
           artefact = get_object_or_404(Artefact, pk=pk)
           artefact.is_archived = True
           artefact.save()
           messages.success(request, f'Artefact "{artefact.title}" archived successfully.')
       except Exception as e:
           messages.error(request, f'Error archiving artefact: {e}')

       return redirect('curator_dashboard')


   @login_required
   def analytics_view(request):
       """Analytics dashboard for curators."""
       if not is_curator(request.user):
           return redirect('/login/?next=/curator/')

       # TODO: Add analytics logic here
       # For now, just render the template
       return render(request, 'curator/analytics.html')
   ```

6. **Save** `museum/views.py`

### Step 2.4: Keep homepage & category views

**Decision:** Since another team member is handling these, we'll leave them in `djangoCode/views.py` for now.

**Action:** No changes needed yet. We'll just update imports later.

---

## 🔗 Phase 3: Fix URL Routing (15 minutes)

### Step 3.1: Update museum/urls.py

**Action:**

1. Open `djangoCode/museum/urls.py`

2. **Remove duplicate login/logout** (lines 6-7)

3. **Add curator URLs**:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       # Privacy & GDPR
       path("privacy/", views.privacy_policy, name="privacy"),
       path("delete-my-data/", views.delete_my_data, name="delete_my_data"),

       # Curator Dashboard & Tools (all require authentication)
       path("curator/dashboard/", views.curator_dashboard, name="curator_dashboard"),
       path("curator/create/", views.create_artefact, name="create_artefact"),
       path("curator/delete/<int:pk>/", views.delete_artefact, name="delete_artefact"),
       path("curator/archive/<int:pk>/", views.archive_artefact, name="archive_artefact"),
       path("curator/analytics/", views.analytics_view, name="analytics_view"),

       # Quiz API
       path("api/quizzes/", views.api_quizzes, name="api_quizzes"),
       path("api/quizzes/<int:quiz_id>/", views.api_quiz_detail, name="api_quiz_detail"),
       path("api/quizzes/<int:quiz_id>/submit/", views.api_quiz_submit, name="api_quiz_submit"),
   ]
   ```

4. **Save** the file

### Step 3.2: Update djangoCode/urls.py (main URL config)

**Action:**

1. Open `djangoCode/djangoCode/urls.py`

2. **Remove curator tool URLs** (lines 32-36) since they're now in museum

3. **Remove duplicate login** (line 38)

4. **Final version should look like:**
   ```python
   from django.contrib import admin
   from django.contrib.auth import views as auth_views
   from django.urls import path, include
   from . import views

   urlpatterns = [
       path("admin/", admin.site.urls),

       # Authentication
       path("login/", auth_views.LoginView.as_view(), name="login"),
       path("logout/", auth_views.LogoutView.as_view(), name="logout"),

       # Homepage & category (keeping in project views for now)
       path("", views.homepage, name="homepage"),
       path("category/", views.category, name="category"),

       # All museum app URLs
       path('', include('museum.urls')),
   ]
   ```

5. **Update djangoCode/djangoCode/views.py** - keep only homepage and category:
   ```python
   from django.shortcuts import render

   def homepage(request):
       return render(request, "main.html")

   def category(request):
       return render(request, "category.html")
   ```

6. **Save both files**

---

## 🗄️ Phase 4: Database Migration (20 minutes)

Now we need to handle the fact that the Artefact model moved from `djangoCode` to `museum`.

### Step 4.1: Remove djangoCode from INSTALLED_APPS

**Action:**

1. Open `djangoCode/djangoCode/settings.py`

2. Find `INSTALLED_APPS` (around line 35)

3. **Remove "djangoCode"** from the list:
   ```python
   INSTALLED_APPS = [
       "django.contrib.admin",
       "django.contrib.auth",
       "django.contrib.contenttypes",
       "django.contrib.sessions",
       "django.contrib.messages",
       "django.contrib.staticfiles",
       # "djangoCode",  ← REMOVE THIS LINE
       "museum",
   ]
   ```

4. **Save** the file

### Step 4.2: Clean Database & Migrations

Since you said you can reset the database and have fixture data, let's start fresh:

**Action:**

```bash
cd 4_code/djangoCode

# 1. Delete old database
rm db.sqlite3

# 2. Delete djangoCode migrations
rm -rf djangoCode/migrations

# 3. Delete old museum migrations (we'll recreate them)
rm museum/migrations/0001_initial.py

# 4. Create fresh migrations for museum app (which now has ALL models)
python manage.py makemigrations museum

# You should see: "Migrations for 'museum': museum/migrations/0001_initial.py"
# This will create Artefact along with all other models

# 5. Apply migrations
python manage.py migrate

# 6. Load fixture data (users, groups, badges, quizzes)
python manage.py loaddata museum/fixtures/seed_data.json

# 7. Verify everything worked
python manage.py shell
```

In the shell, test:
```python
from museum.models import Artefact, Badge, Quiz, UserProfile
from django.contrib.auth.models import User

# Check users
print(User.objects.all())  # Should show Admin and curator_demo

# Check badges
print(Badge.objects.all())  # Should show badges

# Check Artefact model is accessible
print(Artefact.objects.count())  # Should be 0 (no artefacts yet)

# Exit
exit()
```

### Step 4.3: Register Artefact in Admin

**Action:**

1. Open `djangoCode/museum/admin.py`

2. **Add Artefact** to the imports and registration:
   ```python
   from django.contrib import admin

   from .models import (
       UserProfile,
       Badge,
       UserBadge,
       Quiz,
       Question,
       AnswerOption,
       QuizAttempt,
       Response,
       Artefact,  # ADD THIS
   )

   admin.site.register(UserProfile)
   admin.site.register(Badge)
   admin.site.register(UserBadge)
   admin.site.register(Quiz)
   admin.site.register(Question)
   admin.site.register(AnswerOption)
   admin.site.register(QuizAttempt)
   admin.site.register(Response)
   admin.site.register(Artefact)  # ADD THIS
   ```

3. **Save** the file

---

## 🧹 Phase 5: Delete Old Files (5 minutes)

Now that everything is moved and working, clean up:

**Action:**

```bash
cd 4_code/djangoCode

# Delete old model, view, form files from djangoCode
rm djangoCode/models.py
rm djangoCode/forms.py

# Keep djangoCode/views.py (it still has homepage & category)
```

---

## 🧪 Phase 6: Testing (20 minutes)

### Step 6.1: Start the Server

```bash
cd 4_code/djangoCode
python manage.py runserver
```

Open browser: http://127.0.0.1:8000/

### Step 6.2: Test Authentication Flow

**Test Case 1: Visitor Access (No Login)**
1. Go to http://127.0.0.1:8000/
2. Should see homepage ✅
3. Try to access: http://127.0.0.1:8000/curator/dashboard/
4. Should redirect to login page ✅

**Test Case 2: Non-Curator User**
1. Create a regular user via /admin/
2. Login as that user
3. Try to access: http://127.0.0.1:8000/curator/dashboard/
4. Should see error message and redirect ✅

**Test Case 3: Curator Access**
1. Login as "curator_demo" (check fixture for password)
2. Go to: http://127.0.0.1:8000/curator/dashboard/
3. Should see dashboard with artefact lists ✅
4. Try all curator functions:
   - Create artefact
   - Archive artefact
   - Delete artefact
   - View analytics

**Test Case 4: Admin Access**
1. Login as "Admin" (superuser)
2. Access: http://127.0.0.1:8000/curator/dashboard/
3. Should work (staff users are curators) ✅
4. Access: http://127.0.0.1:8000/admin/
5. Should see all models including Artefact ✅

**Test Case 5: Quiz Functionality**
1. As logged-in user, access quiz API:
   - http://127.0.0.1:8000/api/quizzes/
   - Should return JSON with quizzes ✅

### Step 6.3: Common Issues & Fixes

**Issue:** "Template does not exist: curator/dashboard.html"
**Fix:** The template hasn't been created yet. For now, create a simple one:
```bash
mkdir -p templates/curator
```

Create `templates/curator/dashboard.html`:
```html
{% extends "base.html" %}

{% block content %}
<h1>Curator Dashboard</h1>

<section>
    <h2>Active Artefacts</h2>
    {% if active_artefacts %}
        <ul>
        {% for artefact in active_artefacts %}
            <li>
                {{ artefact.title }} - {{ artefact.domain }}
                <a href="{% url 'archive_artefact' artefact.pk %}">Archive</a>
                <a href="{% url 'delete_artefact' artefact.pk %}">Delete</a>
            </li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No active artefacts.</p>
    {% endif %}
</section>

<section>
    <h2>Archived Artefacts</h2>
    {% if archived_artefacts %}
        <ul>
        {% for artefact in archived_artefacts %}
            <li>{{ artefact.title }} - {{ artefact.domain }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No archived artefacts.</p>
    {% endif %}
</section>

<a href="{% url 'create_artefact' %}">Create New Artefact</a>
<a href="{% url 'analytics_view' %}">View Analytics</a>
{% endblock %}
```

**Issue:** "No module named 'museum.forms'"
**Fix:** Make sure you created `museum/forms.py` in Step 2.2

**Issue:** Import errors in views
**Fix:** Check all imports at the top of `museum/views.py` are correct

---

## ✅ Phase 7: Commit Your Changes (5 minutes)

Once everything is working:

```bash
# Check what changed
git status

# Add all changes
git add .

# Commit with descriptive message
git commit -m "Integration complete: Consolidated structure and added security

- Moved Artefact model from djangoCode to museum app
- Moved curator views to museum app with authentication
- Added @login_required and is_curator() checks to all curator functions
- Merged duplicate curator_dashboard implementations
- Cleaned up URL routing (removed duplicates)
- Removed djangoCode from INSTALLED_APPS
- Registered Artefact in admin panel
- Reset migrations with all models in museum app
- All tests passing"

# Push to remote
git push origin Curator-Security-Model-MERGE
```

---

## 📝 Summary of Changes

### Files Moved:
- `djangoCode/models.py` → `museum/models.py` (Artefact model)
- `djangoCode/forms.py` → `museum/forms.py` (ArtefactForm)
- Curator functions from `djangoCode/views.py` → `museum/views.py`

### Files Modified:
- `museum/views.py` - Added curator functions with security
- `museum/urls.py` - Added curator URL patterns
- `museum/admin.py` - Registered Artefact
- `djangoCode/urls.py` - Removed curator URLs, kept auth + includes
- `djangoCode/views.py` - Kept only homepage & category
- `djangoCode/settings.py` - Removed "djangoCode" from INSTALLED_APPS

### Files Deleted:
- `djangoCode/models.py`
- `djangoCode/forms.py`
- `djangoCode/migrations/`
- `db.sqlite3` (recreated fresh)

### Security Added:
- ✅ `@login_required` on all curator functions
- ✅ `is_curator()` check on all curator functions
- ✅ Proper redirects for unauthorized access
- ✅ User-friendly error messages

### Structure Fixed:
- ✅ All models in `museum/models.py`
- ✅ All views in `museum/views.py` (except homepage/category)
- ✅ All forms in `museum/forms.py`
- ✅ No duplicate URLs
- ✅ djangoCode is project settings only
- ✅ museum is the application

---

## 🎯 Next Steps (After This Integration)

1. **Create Exhibit Model** (for full spec compliance)
   - Add richer exhibit fields
   - Link Artefacts to Exhibits

2. **Enhance Templates**
   - Better curator dashboard UI
   - Create artefact form page
   - Analytics visualization

3. **Add Tests**
   - Unit tests for models
   - Integration tests for views
   - Test security (unauthorized access)

4. **Frontend Work**
   - Homepage design (team member's responsibility)
   - Category page design
   - Visitor exhibit browsing

---

## 🆘 Troubleshooting

### "Django not installed" error
- Make sure venv is activated: `source .venv/bin/activate`
- Check which Python: `which python` (should be in .venv)
- Reinstall: `pip install -r 4_code/requirements.txt`

### "No such table" errors
- Run migrations: `python manage.py migrate`
- If still broken, delete db.sqlite3 and start over

### Template errors
- Check TEMPLATES 'DIRS' in settings.py
- Make sure templates/ folder exists
- Create minimal templates for testing

### Import errors
- Check all imports use relative imports: `from .models import X`
- Make sure files are saved
- Restart the server

### Permission denied on curator pages
- Check user is in "Curator" group: Django admin → Users
- Check is_curator() function is working
- Try with Admin user (should always work)

---

## 📞 Need Help?

If you get stuck on any step:
1. Check the error message carefully
2. Look at the "Common Issues" sections
3. Use `python manage.py shell` to test imports
4. Ask me to explain any step in more detail!


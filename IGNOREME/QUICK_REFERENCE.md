# Quick Reference Guide - Common Commands

**Quick access to commands you'll need during integration**

---

## 📍 Navigation

```bash
# From anywhere, go to project root
cd ~/Documents/GitHub/Ai-Failure-Museum

# From root, go to Django project
cd 4_code/djangoCode

# From djangoCode, back to root
cd ../..
```

---

## 🔧 Virtual Environment

```bash
# Activate venv (from project ROOT)
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Deactivate venv
deactivate

# Check which Python (should show .venv path)
which python    # Mac/Linux
where python    # Windows

# Check installed packages
pip list

# Install/reinstall requirements
pip install -r requirements.txt
```

---

## 🗄️ Database Commands

```bash
# From 4_code/djangoCode/

# Create migrations (after model changes)
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Load fixture data
python manage.py loaddata museum/fixtures/seed_data.json

# Dump data to fixture
python manage.py dumpdata museum > backup.json

# Reset database (delete all data)
rm db.sqlite3              # Mac/Linux
del db.sqlite3             # Windows
python manage.py migrate
python manage.py loaddata museum/fixtures/seed_data.json
```

---

## 👤 User Management

```bash
# Create superuser
python manage.py createsuperuser

# Django shell (for manual testing)
python manage.py shell
```

**In shell:**
```python
from django.contrib.auth.models import User, Group
from museum.models import *

# Check users
User.objects.all()

# Create user
user = User.objects.create_user('username', 'email@example.com', 'password')

# Add user to Curator group
curator_group = Group.objects.get(name='Curator')
user.groups.add(curator_group)
user.save()

# Check if user is curator
from museum.rbac import is_curator
is_curator(user)

# Exit shell
exit()
```

---

## 🚀 Server Commands

```bash
# Start development server
python manage.py runserver

# Start on different port
python manage.py runserver 8001

# Stop server
Ctrl + C
```

---

## 🧪 Testing Commands

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test museum

# Run specific test file
python manage.py test museum.tests.test_models

# Run specific test class
python manage.py test museum.tests.test_models.ArtefactModelTest

# Run specific test method
python manage.py test museum.tests.test_models.ArtefactModelTest.test_artefact_creation

# Verbose output
python manage.py test -v 2

# Keep test database (for inspection)
python manage.py test --keepdb
```

---

## 📝 File Operations (Integration Tasks)

```bash
# From project root

# Move requirements.txt to root
mv 4_code/requirements.txt requirements.txt

# Create directories
mkdir -p museum/tests

# Create empty file
touch filename              # Mac/Linux
type nul > filename         # Windows

# Delete file
rm filename                 # Mac/Linux
del filename                # Windows

# Delete directory
rm -rf dirname              # Mac/Linux
rmdir /s dirname            # Windows

# Copy file
cp source dest              # Mac/Linux
copy source dest            # Windows
```

---

## 🔍 Git Commands

```bash
# Check current branch
git branch --show-current

# Create backup branch
git branch backup-before-integration

# Check status
git status

# See what changed
git diff

# Stage all changes
git add .

# Stage specific file
git add path/to/file.py

# Commit
git commit -m "Description of changes"

# Push to remote
git push origin branch-name

# See commit history
git log --oneline -10

# Discard changes to file (CAREFUL!)
git checkout -- path/to/file

# See what's in staging
git diff --staged
```

---

## 🔎 Debugging Commands

```bash
# Check for Python syntax errors
python -m py_compile path/to/file.py

# Import check
python -c "from museum.models import Artefact; print('OK')"

# Django check (find issues)
python manage.py check

# Show URLs
python manage.py show_urls  # If django-extensions installed

# Find files
find . -name "*.py" | grep models

# Search in files
grep -r "Artefact" museum/

# Check Django version
python -c "import django; print(django.get_version())"
```

---

## 📊 Inspection Commands

```bash
# List installed apps
python manage.py diffsettings | grep INSTALLED_APPS

# SQL for migration
python manage.py sqlmigrate museum 0001

# Database shell
python manage.py dbshell

# Check static files
python manage.py findstatic filename.css
```

---

## 🧹 Cleanup Commands

```bash
# Remove Python cache
find . -type d -name "__pycache__" -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Remove migration files (CAREFUL!)
rm museum/migrations/0*.py

# Remove database
rm db.sqlite3
```

---

## 🔧 Integration-Specific Checklist

```bash
# 1. Backup
git add .
git commit -m "Pre-integration backup"
git branch backup-before-integration

# 2. Move requirements.txt
mv 4_code/requirements.txt requirements.txt

# 3. Delete old migrations
rm db.sqlite3
rm -rf djangoCode/migrations
rm museum/migrations/0001_initial.py

# 4. Create fresh migrations
cd 4_code/djangoCode
python manage.py makemigrations museum

# 5. Apply migrations
python manage.py migrate

# 6. Load data
python manage.py loaddata museum/fixtures/seed_data.json

# 7. Test
python manage.py runserver
# Open http://127.0.0.1:8000/

# 8. Run tests
python manage.py test

# 9. Commit
git add .
git commit -m "Integration complete"
```

---

## 🆘 Emergency Commands

### Something went wrong!

```bash
# Restore from git
git checkout -- .

# Go back to specific commit
git log --oneline  # Find commit hash
git checkout <commit-hash>

# Restore from backup branch
git checkout backup-before-integration

# Start fresh from clean slate
git stash  # Save current changes
git checkout main
git pull origin main
```

### Django won't start

```bash
# Check for syntax errors
python manage.py check

# Reinstall Django
pip uninstall django
pip install Django==6.0.2

# Check settings
python manage.py diffsettings | less
```

### Tests failing

```bash
# Run specific failing test with verbosity
python manage.py test museum.tests.test_models.ArtefactModelTest.test_artefact_creation -v 3

# Drop into debugger on failure
python manage.py test --pdb

# Keep test database for inspection
python manage.py test --keepdb
```

---

## 📋 Pre-Integration Checklist

Before starting integration:
- [ ] Virtual environment activated
- [ ] Django installed (`python -c "import django"` works)
- [ ] On correct branch: `Curator-Security-Model-MERGE`
- [ ] Backup created: `git branch backup-before-integration`
- [ ] All uncommitted work committed
- [ ] Read INTEGRATION_ACTION_PLAN.md

---

## 📋 Post-Integration Checklist

After completing integration:
- [ ] Server starts without errors
- [ ] Homepage loads (http://127.0.0.1:8000/)
- [ ] Admin panel works (http://127.0.0.1:8000/admin/)
- [ ] Curator login required for `/curator/dashboard/`
- [ ] Regular user can't access curator tools
- [ ] Curator can create/archive/delete artefacts
- [ ] All tests pass (`python manage.py test`)
- [ ] Changes committed to git
- [ ] README updated

---

## 🎯 Quick Troubleshooting

| Problem | Quick Fix |
|---------|-----------|
| "Django not installed" | `pip install -r requirements.txt` |
| "No module named museum" | Make sure you're in `4_code/djangoCode` |
| "No such table" | `python manage.py migrate` |
| "Template does not exist" | Check `TEMPLATES` in settings.py |
| Server won't start | Check another isn't running on :8000 |
| Permission denied | Check user in Curator group |
| Import error | `python manage.py check` |
| Git merge conflict | Read conflict markers, choose version |

---

## 📞 When You're Stuck

1. Read the error message carefully
2. Check you're in the right directory
3. Check venv is activated
4. Try `python manage.py check`
5. Check recent commits: `git log --oneline -5`
6. Ask for help with specific error message

---

## 🔗 Useful URLs

- **Homepage:** http://127.0.0.1:8000/
- **Admin:** http://127.0.0.1:8000/admin/
- **Login:** http://127.0.0.1:8000/login/
- **Curator Dashboard:** http://127.0.0.1:8000/curator/dashboard/
- **Quiz API:** http://127.0.0.1:8000/api/quizzes/
- **Privacy:** http://127.0.0.1:8000/privacy/

---

## 💡 Pro Tips

**Activate venv automatically:**
Add to `~/.bashrc` or `~/.zshrc`:
```bash
alias museum='cd ~/Documents/GitHub/Ai-Failure-Museum && source .venv/bin/activate && cd 4_code/djangoCode'
```

Then just type: `museum` to activate and navigate!

**Quick test shortcut:**
```bash
alias test-museum='python manage.py test -v 2'
```

**Quick server restart:**
```bash
alias run-museum='python manage.py runserver'
```


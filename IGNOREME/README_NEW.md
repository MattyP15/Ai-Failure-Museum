# AI Failure Museum

**University of Exeter - 2nd Year Group Project**

An interactive web application showcasing notable AI system failures to educate visitors about AI limitations and promote responsible AI development. Built with Django.

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Manual Setup](#manual-setup)
- [Running the Application](#running-the-application)
- [User Accounts](#user-accounts)
- [Admin Functions](#admin-functions)
- [Database Management](#database-management)
- [Project Structure](#project-structure)
- [For Examiners](#for-examiners)

---

## 🚀 Quick Start

### Automatic Setup (Windows)

```bash
start_museum.bat
```

### Automatic Setup (Mac/Linux)

```bash
# First time only - grant execute permission
chmod +x start_museum.sh

# Run the script
./start_museum.sh
```

---

## 🔧 Manual Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/MattyP15/Ai-Failure-Museum.git
cd Ai-Failure-Museum
```

### 2. Create Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

💡 **Note:** Your virtual environment is in the **root folder**, not in djangoCode!

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- Django 6.0.2
- python-dotenv 1.2.1
- Other required packages

### 4. Configure Environment Variables

**Windows:**
```bash
copy 4_code\djangoCode\djangoCode\.env.example 4_code\djangoCode\djangoCode\.env
```

**Mac/Linux:**
```bash
cp 4_code/djangoCode/djangoCode/.env.example 4_code/djangoCode/djangoCode/.env
```

Then edit `.env` and set a secure `SECRET_KEY` (any random string).

### 5. Navigate to Django Project

```bash
cd 4_code/djangoCode
```

### 6. Initialize Database

```bash
# Create database tables
python manage.py migrate

# Load demo data (users, badges, quizzes)
python manage.py loaddata museum/fixtures/seed_data.json
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Open your browser to: **http://127.0.0.1:8000/**

---

## 🎮 Running the Application

### Starting the Server

From the project root with venv activated:

```bash
cd 4_code/djangoCode
python manage.py runserver
```

### Stopping the Server

Press `Ctrl + C` in the terminal

---

## 👥 User Accounts

### Default Demo Accounts

The `seed_data.json` fixture includes these accounts:

#### Admin (Superuser)
- **Username:** `Admin`
- **Password:** `Ric3Sh0wer`
- **Access:** Full admin panel access, curator tools, all features

#### Curator Demo
- **Username:** `curator_demo`
- **Password:** `P4ace_CHA5er`
- **Access:** Curator dashboard, create/edit/archive artefacts, analytics

⚠️ **Security Note:** Change these passwords before deploying to production!

### Key URLs

- **Home:** http://127.0.0.1:8000/
- **Login:** http://127.0.0.1:8000/login/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Curator Dashboard:** http://127.0.0.1:8000/curator/dashboard/ *(requires curator login)*
- **Privacy Policy:** http://127.0.0.1:8000/privacy/
- **Delete My Data:** http://127.0.0.1:8000/delete-my-data/ *(requires login)*

---

## 🔐 Admin Functions

Access the admin panel at http://127.0.0.1:8000/admin/ with admin credentials.

### Create New Users

1. Go to **Admin Panel** → **Users** → **Add User +**
2. Enter username and password
3. Click **SAVE**
4. (Optional) Fill in additional details like email, first/last name
5. Click **SAVE** again

### Assign Curator Role

To give a user curator permissions:

1. Go to **Admin Panel** → **Users**
2. Click on the username
3. Scroll to **Groups** section
4. Double-click **"Curator"** to move it to "Chosen groups"
5. Click **SAVE**

Now that user can access curator tools at `/curator/dashboard/`

### Create Badges (Gamification)

1. Go to **Admin Panel** → **Badges** → **Add Badge**
2. Fill in:
   - **Code:** Unique identifier (e.g., `first_steps`)
   - **Name:** Display name (e.g., `First Steps`)
   - **Description:** What this badge is for
   - **Points threshold:** Points required to earn (e.g., 10)
3. Click **SAVE**

Users automatically receive badges when their points reach the threshold.

### Create Quizzes

1. Go to **Admin Panel** → **Quizzes** → **Add Quiz**
2. Fill in:
   - **Title:** Quiz name
   - **Description:** What this quiz covers
   - **Is Active:** ✓ (checked)
   - **Points for completion:** Points awarded (e.g., 10)
3. Click **SAVE**

### Add Questions to Quiz

1. Go to **Admin Panel** → **Questions** → **Add Question**
2. Fill in:
   - **Quiz:** Select your quiz
   - **Prompt:** The question text
   - **Qtype:**
     - `text` for reflective/open-ended questions
     - `mc` for multiple choice
   - **Order:** Display order (0, 1, 2, etc.)
3. Click **SAVE**

For multiple choice questions, also add **Answer Options**:
1. **Admin Panel** → **Answer Options** → **Add Answer Option**
2. Link to your question and add option text
3. Repeat for each choice

---

## 🗄️ Database Management

### Reset Database (Delete All Data)

⚠️ **Warning:** This deletes ALL users, exhibits, quizzes, and data!

```bash
# Stop the server first (Ctrl+C)

# Navigate to djangoCode
cd 4_code/djangoCode

# Delete the database file
rm db.sqlite3  # Mac/Linux
del db.sqlite3  # Windows

# Recreate database structure
python manage.py migrate

# Reload demo data
python manage.py loaddata museum/fixtures/seed_data.json
```

### Create New Superuser

If you deleted the admin account:

```bash
python manage.py createsuperuser
```

Follow the prompts:
- Username: (your choice)
- Email: (can be blank - just press Enter)
- Password: (enter twice)

---

## 📁 Project Structure

```
Ai-Failure-Museum/
│
├── .venv/                          # Virtual environment (ROOT level)
├── requirements.txt                # Python dependencies (ROOT level)
│
├── 4_code/
│   └── djangoCode/                 # Django project folder
│       ├── manage.py               # Django management script
│       │
│       ├── djangoCode/             # Project settings (NOT an app)
│       │   ├── settings.py         # Project configuration
│       │   ├── urls.py             # Root URL routing
│       │   ├── wsgi.py             # WSGI entry point
│       │   ├── .env                # Environment variables (SECRET_KEY)
│       │   └── views.py            # Homepage & category views only
│       │
│       ├── museum/                 # Main application (ALL logic here)
│       │   ├── models.py           # Database models (Artefact, Quiz, etc.)
│       │   ├── views.py            # View functions (curator tools, quiz API)
│       │   ├── forms.py            # Django forms
│       │   ├── urls.py             # App URL patterns
│       │   ├── admin.py            # Admin panel configuration
│       │   ├── rbac.py             # Role-based access control
│       │   ├── gamification.py     # Points and badges logic
│       │   ├── signals.py          # Auto-create user profiles
│       │   ├── migrations/         # Database migrations
│       │   └── fixtures/           # Demo data (seed_data.json)
│       │
│       ├── templates/              # HTML templates
│       ├── static/                 # CSS, JavaScript, images
│       ├── media/                  # User-uploaded files (artefacts)
│       └── db.sqlite3              # SQLite database
│
├── 0_admin/                        # Project admin files
├── 1_report/                       # Project reports
├── 2_handover_pack/                # Handover documentation
├── 3_ethics_and_licensing/         # Ethics & licensing docs
├── 5_presentation/                 # Presentation materials
│
├── start_museum.bat                # Windows startup script
├── start_museum.sh                 # Mac/Linux startup script
└── README.md                       # This file
```

### Key Concepts

**djangoCode/djangoCode/** = Project Settings Folder
- Contains only configuration and routing
- NOT a Django app

**djangoCode/museum/** = Main Application
- Contains all models, views, business logic
- This is where code lives

---

## 🎓 For Examiners

### Quick Demo Setup

Use the automatic scripts for fastest setup:

**Windows:** Run `start_museum.bat`
**Mac/Linux:** Run `./start_museum.sh` (after `chmod +x start_museum.sh`)

Or follow the [Manual Setup](#manual-setup) instructions above.

### Demo Credentials

- **Admin:** Username `Admin`, Password `Ric3Sh0wer`
- **Curator:** Username `curator_demo`, Password `P4ace_CHA5er`

### Features to Test

#### Visitor Features (No Login Required)
- Browse homepage
- View exhibits *(once implemented)*
- Take quizzes via API: http://127.0.0.1:8000/api/quizzes/

#### Curator Features (Requires Curator Login)
- Access: http://127.0.0.1:8000/curator/dashboard/
- Create artefacts
- Archive artefacts (hide from visitors)
- Delete artefacts
- View analytics *(once implemented)*

#### Security Features
- Try accessing `/curator/dashboard/` without login → redirects to login
- Login as non-curator user → denied access with error message
- All curator functions protected by authentication

#### Gamification Features (Requires Login)
- Take quiz via API: POST to `/api/quizzes/1/submit/`
- Earn points for quiz completion
- Automatically receive badges when point thresholds reached
- View earned badges in admin panel

#### Privacy/GDPR Features
- View privacy policy: http://127.0.0.1:8000/privacy/
- Delete account data: http://127.0.0.1:8000/delete-my-data/

---

## 🔧 Development Notes

### Virtual Environment

Always activate the virtual environment before working:

```bash
# From project root
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

Your terminal prompt should show `(.venv)` when activated.

### Making Database Changes

After modifying models in `museum/models.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating Fixtures (Backup Data)

To export current database to JSON:

```bash
# Export all museum app data
python manage.py dumpdata museum > museum/fixtures/my_backup.json

# Export specific models
python manage.py dumpdata auth.User > backup_users.json
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test museum

# Run with verbosity
python manage.py test -v 2
```

---

## 📝 Contributing

This is a university group project. Team members should:

1. Create feature branches from `main`
2. Work on assigned features
3. Test thoroughly before merging
4. Coordinate with integration lead for merges

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/my-feature

# Make changes, test, commit
git add .
git commit -m "Description of changes"

# Push to remote
git push origin feature/my-feature

# Create pull request for review
```

---

## 🆘 Troubleshooting

### "Django not installed" error
- Make sure venv is activated: Check for `(.venv)` in terminal
- Reinstall: `pip install -r requirements.txt`

### "No such table" errors
- Run migrations: `python manage.py migrate`

### "Module not found" errors
- Check you're in the right directory: `4_code/djangoCode`
- Check venv is activated
- Reinstall requirements

### Server won't start
- Check another server isn't running on port 8000
- Try: `python manage.py runserver 8001` (different port)

### "Permission denied" on curator pages
- Make sure you're logged in
- Check user is in "Curator" group (via admin panel)
- Admin users (is_staff=True) automatically have curator access

---

## 📧 Contact

For issues or questions, contact the development team or course instructor.

---

## 📄 License

This is an educational project for University of Exeter.
See `3_ethics_and_licensing/` for full details.


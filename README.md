# AI Failure Museum

**Learning from AI's Failures in Environmental Decision-Making**

A Django web application that presents curated case studies of AI failures across 8 categories, with reflective quizzes, curator tools, and engagement analytics.

**Live Site:** https://ai-failure-museum.onrender.com/  
**Scrumboard Link** https://teamhlscrumboard.atlassian.net/jira/core/projects/TH/board
**Module:** COMM2020 Team Project — University of Exeter  
**Licence:** MIT  

---

## Team Members & Contributions

| Name | Student ID | Role | Key Contributions |
|------|-----------|------|-------------------|
| Hyam Ali | 740092404 | Project Leader | Scope management, 20 exhibit case studies, 40 quizzes (200 questions), 20 artefact visualisations, JSON fixture data, CW2 documentation |
| Luqman Abdinasir | 730059660 | Scrum Master | Sprint planning, Jira board management, task allocation, login/register page styling, quiz CSS |
| Kate Walton | 740068456 | Django Developer | Models (Category, Comment, Bookmark, UserSubmission), curator dashboard, archiving, community submissions, view tracking, privacy pages, fixtures |
| Osama Zein | 740045326 | Django Developer / Bug Fixer | Artefact uploads, timeline events, quiz enhancements, deployment config, Accounts.json, migration fixes |
| Louis Souttar-Stone | 740015771 | HTML Developer | Dashboard UI with filtering, login redesign, CSS separation, mobile responsiveness, analytics UI, points system |
| Pyae Thaw | 720096583 | HTML/Django Developer | Auth & RBAC, gamification (points/badges), privacy delete-my-data, seed data fixtures, user tracking |
| Stanislaw Sienczewski | 730051430 | HTML/Django Developer | Initial requirements documents (Sprint 1) |

---

## Quick Start

### Windows

1. `python3 -m venv .venv`
2. `.venv\Scripts\activate`
3. `pip install -r requirements.txt`
4. `cd 4_code\djangoCode`
5. `python manage.py migrate`
6. `python manage.py loaddata museum/fixtures/Accounts.json museum/fixtures/categories.json museum/fixtures/exhibits.json museum/fixtures/quizzes.json`
7. `python manage.py runserver`

### Linux / Mac

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cd 4_code/djangoCode`
5. `python3 manage.py migrate`
6. `python3 manage.py loaddata museum/fixtures/Accounts.json museum/fixtures/categories.json museum/fixtures/exhibits.json museum/fixtures/quizzes.json`
7. `python3 manage.py runserver`

Or just run: `python3 launch.py`

Open browser at http://127.0.0.1:8000/

---

## Demo Account Credentials

| Role | Username | Password |
|------|----------|----------|
| Admin (Superuser) | Admin | Ric3Sh0wer |
| Curator | curator_demo | P4ace_CHASer |
| Visitor | visitor | password123 |

---

## Important URLs

- **Home:** http://127.0.0.1:8000/
- **Admin Panel:** http://127.0.0.1:8000/admin/
- **Login:** http://127.0.0.1:8000/login/
- **Curator Dashboard:** http://127.0.0.1:8000/curator/dashboard/
- **Analytics:** http://127.0.0.1:8000/curator/analytics/
- **Privacy Policy:** http://127.0.0.1:8000/privacy/
- **Accessibility:** http://127.0.0.1:8000/accessibility/

---

## Key Features

- 20 exhibits across 8 failure categories (Environmental, Healthcare, Law, Economic, Safety-Critical, Misinformation, Bias, Privacy)
- 40 reflective quizzes with 200 multiple-choice questions
- 20 supporting data visualisation artefacts
- Curator dashboard with exhibit create/edit/archive, quiz editor, and analytics
- Community submission system with curator review pool
- Bookmarking, commenting, and timeline events
- Points and badge gamification system
- Role-based access control (Visitor, Curator, Admin)
- Privacy policy, terms of service, accessibility page, and delete-my-data mechanism
- Deployed on Render with PostgreSQL (production) and SQLite (development)

---

## Managing Users

### Adding a User to the Curator Group

1. Go to http://127.0.0.1:8000/admin/
2. Click "Users" → Select the user
3. Scroll to "Groups" → Double-click "Curators"
4. Click SAVE

### Create New Superuser

```
cd 4_code/djangoCode
python3 manage.py createsuperuser
```

---

## Run Tests

```
python manage.py test
```

Run a specific test:
```
python manage.py test museum.tests.test_rbac
```

Test files cover: RBAC permissions, gamification, form validation, curator view access, quiz API submission, and data deletion.

---

## Reset Database

```
cd 4_code/djangoCode
rm db.sqlite3
python3 manage.py migrate
python3 manage.py loaddata museum/fixtures/Accounts.json museum/fixtures/categories.json museum/fixtures/exhibits.json museum/fixtures/quizzes.json
```

---

## Repository Structure

```
Ai-Failure-Museum/
├── README.md
├── requirements.txt
├── build.sh / Procfile / render.yaml    ← Render deployment config
├── launch.py                            ← Convenience local startup script
├── 0_admin/                             ← Submission metadata, dev log
├── 1_report/                            ← CW2 final report
├── 2_handover_pack/                     ← Client handover documentation
├── 3_ethics_and_licensing/              ← Licence, ethics docs
├── 4_code/djangoCode/                   ← Django project root
│   ├── djangoCode/                      ← Settings, URLs, WSGI
│   ├── museum/                          ← Main app (models, views, forms, RBAC)
│   │   ├── fixtures/                    ← Seed data (JSON)
│   │   ├── tests/                       ← 7 automated test files
│   │   ├── management/                  ← Custom management commands
│   │   └── templatetags/                ← Custom template tags
│   ├── templates/                       ← HTML templates
│   ├── static/                          ← CSS, JS, images
│   └── media/exhibits/artefacts/        ← Uploaded artefact images
├── 5_presentation/                      ← Demo slides
└── GroupHL_CW1/                         ← Sprint 1 submission archive
```

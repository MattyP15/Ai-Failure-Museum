/// THIS IS A MERGE OF THREE BRANCHES:
/// - curator-tools
/// - Artefact-model
/// - Security-and-Interaction

# AI-Failure-Museum

==== Instructions for quickstart ====

-- WINDOWS --

1. python3 -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. cd 4_code\djangoCode
5. python manage.py migrate
6. python manage.py loaddata museum/fixtures/demo_data.json
7. python manage.py runserver


-- Linux / Mac --

1. python3 -m venv .venv
2. source .venv/bin/activate
3. pip install -r requirements.txt
4. cd 4_code/djangoCode
5. python3 manage.py migrate
5. python3 manage.py loaddata museum/fixtures/demo_data.json
6. python3 manage.py runserver


Open browser at http://127.0.0.1:8000/


==== Account Credentials ====

-- Admin (Superuser) --

* Username : 'Admin'
* Password : 'Ric3Sh0wer'

-- Curator Demo --

* Username : 'curator_demo'
* Password : 'P4ace_CHASer'

-- Visitor --

* Username : 'visitor'
* Password : 'password123'


==== Important URLS ====

- Home: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/login/
- Curator Dashboard: http://127.0.0.1:8000/curator/dashboard/
- Privacy Policy: http://127.0.0.1:8000/privacy/


==== Managing Users ====

-- Adding User to Curator Group --

1. Go to http://127.0.0.1:8000/admin/
2. Click "Users" -> Select user
3. Scroll to "Groups" -> Double-click "Curators"
4. Click SAVE


-- Create New Superuser ---

cd 4_code/djangoCode
python3 manage.py createsuperuser


==== Reset Database ====

// stop server (Ctrl+C)
cd 4_code/djangoCode
rm db.sqlite3
python3 manage.py migrate
python3 manage.py loaddata museum/fixtures/demo_data.json


=== Run Tests ===

Run Pytest : python manage.py test

Run Full Django Test Suite: python manage.py test

Run Specific test: python manage.py test museum.tests.<<Insert Test>>
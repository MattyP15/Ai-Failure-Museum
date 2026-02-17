/// THIS IS A MERGE OF THREE BRANCHES: 
/// - curator-tools
/// - Artefact-model
/// - Security-and-Interaction

# AI-Falure-Museum 

==== Instructions for quickstart ====

-- WINDOWS --

.venv\Scripts\activate 
pip install -r requirements.txt
cd 4_code\djangoCode
python manage.py migrate
<<<<<<< Updated upstream
python manage.py loaddata museum/fixtures/seed_data.json
python3 manage.py loaddata museum/fixtures/demo_data.json
=======
python manage.py loaddata museum/fixtures/demo_data.json
python set_passwords.py
>>>>>>> Stashed changes
python manage.py runserver


-- Linux / Mac --

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd 4_code/djangoCode
<<<<<<< Updated upstream
python manage.py migrate
python manage.py loaddata museum/fixtures/seed_data.json
python manage.py loaddata museum/fixtures/demo_data.json
python manage.py runserver

=======
python3 manage.py migrate
python3 manage.py loaddata museum/fixtures/demo_data.json
python3 set_passwords.py
python3 manage.py runserver


(wait 5 seconds after pasting to hit enter)
>>>>>>> Stashed changes
Open browser at http://127.0.0.1:8000/


==== Admin Credentials ====

-- Admin (Superuser) -- 

* Username : 'Admin'
* Password : 'Ric3Sh0wer'

-- Curator Demo --

* Username : 'curator_demo'
* Password : 'P4ace_CHASer' 

<<<<<<< Updated upstream
=======
-- Visitor --
* username : 'visitor'
* password : 'password123'

>>>>>>> Stashed changes

==== Important URLS ====

- Home: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/
- Login: http://127.0.0.1:8000/login/
- Curator Dashboard: http://127.0.0.1:8000/curator/dashboard/
- Privacy Policy: http://127.0.0.1:8000/privacy/


==== Managing users ====

-- setup demo users --
python3 manage.py setup_demo_users


-- Adding User to Curator Group --

1. Go to http://127.0.0.1:8000/admin/
2. Click "Users" → Select user
3. Scroll to "Groups" → Double-click "Curator"
4. Click SAVE


-- Create New Superuser ---

cd 4_code/djangoCode
python manage.py createsuperuser


==== Reset Database ====

// stop server (Ctrl +C) 
cd 4_code/djangoCode
rm db.sqlite3
python manage.py migrate
python manage.py loaddata museum/fixtures/seed_data.json
python manage.py loaddata museum/fixtures/demo_data.json


```
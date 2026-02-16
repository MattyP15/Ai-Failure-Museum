# Ai-Failure-Museum
Teamwork project for University of exeter 2nd year.


To run server locally do:

Windows:
python -m venv .venv
.venv\Scripts\activate 
cd Ai-Failure-Museum-main\4_code\djangoCode
pip install -r requirements.txt
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver



Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate
cd Ai-Failure-Museum-main/4_code/djangoCode
pip install -r requirements.txt
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Load demo data:
python manage.py migrate
python manage.py loaddata seed_data


Links:
Home: http://127.0.0.1:8000/ 
Admin: http://127.0.0.1:8000/admin/
Login: http://127.0.0.1:8000/login/
Curator page (protected): http://127.0.0.1:8000/curator/
Privacy policy page: http://127.0.0.1:8000/privacy/
Delete my data (must be logged in): http://127.0.0.1:8000/delete-my-data/
[try not to delete the admin account]


Admin Details:
Username: Admin
Password: Ric3Sh0wer

Curator Demo: Details:
Username : curator_demo
Password : P4ace_CHA5er

Add Your own Users:
Go to http://127.0.0.1:8000/admin/
Click on "Users" in "Authentication and Authorization"
Click on "Add User +" on the top right
Assign username and password
Click on "SAVE"

Assign a User to be a curator:
Go to http://127.0.0.1:8000/admin/
Click on "Users" in "Authentication and Authorization"
Select a user and click on the username
Scroll to group and double click on "Curator"
Click on SAVE

Create badges:
Go to http://127.0.0.1:8000/admin/
Click on Badges
Click on Add
Fill "Code","Name", and "Points threshold"
Click on SAVE

Create a quizz and a question:
Go to http://127.0.0.1:8000/admin/
Click on "Quiz" and "ADD QUIZ"
Fill the "Title", "Description", check "Is Active", and set "Points for completion"
Click SAVE
Click Question and find you quizz
Select Qtype
Click SAVE

Reset the database ( this will delete every account,quizz and any other data stored):
Stop server (ctrl+c)
Delete db.sqlite3
rerun migrations:
python manage.py migrate
python manage.py createsuperuser

Create an Admin ( in case you've deleted it"): 
python manage.py createsuperuser
follow the instructions given by the terminal
(email can be blank) 

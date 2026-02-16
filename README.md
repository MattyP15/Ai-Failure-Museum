/// THIS IS A MERGE OF THREE BRANCHES: 
/// - curator-tools
/// - Artefact-model
/// - Security-and-Interaction


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
cd 4_code/djangoCode
python3 manage.py runserver




FOR EXAMINER: 

Below are automatic and manual instructions to run the museum site

======== Automatic ======== 

-- Windows --

run start_museum.bat 
Enter password when promted

-- Mac/ Linux --

[for mac only] run 'chmod +x start_museum.sh' in your terminal once to give the file permission to run. 

run start_museum.sh 
Enter password when promted


======== MANUAL ======== 

== Instalation and Setup == 
1. Clone repository 

    git clone https://github.com/MattyP15/Ai-Failure-Museum

2. Copy the contents of '.env.example' into a file called '.env', then enter a random (secure) password for the SECRET_KEY

3. Set up the venv 

    -- Windows -- 
    python -m venv .venv
    .venv\Scripts\activate

    -- Mac / Linux --
    python3 -m venv .venv
    source .venv/bin/activate


4. Install dependancies 

    pip install -r requirements.txt


5. Configure Enviroment Variables 

    -- Windows -- 
    copy .env.example .env

    -- Mac / Linux --
    cp .env.example .env


6. Initialise the seeded data

    python manage.py migrate
    python manage.py loaddata seeded_data.json ####IF FILE NAME IS seeded_data     

7. Run the Museum 

    python manage.py runserver 


Once the server is running, open browser and go to [http://127.0.0.1:8000/] (http://127.0.0.1:8000/)



== Curator Dashboad ==

To test the curator features, use the following demo credentials:

## example credentials 
Username : curator_demo
Password : Password123 
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

# Ai-Failure-Museum
Teamwork project for University of exeter 2nd year.


To run server locally do:
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
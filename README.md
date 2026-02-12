# Ai-Failure-Museum
Teamwork project for University of exeter 2nd year.


To run server locally do:
source .venv/bin/activate
cd 4_code/djangoCode
python3 manage.py runserver




FOR EXAMINER: 

== Instalation and Setup == 
1. Clone repository 

    git clone https://github.com/MattyP15/Ai-Failure-Museum


2. Set up the venv 

    -- Windows -- 
    python -m venv .venv
    .venv\Scripts\activate

    -- Mac / Linux --
    python3 -m venv .venv
    source .venv/bin/activate


3. Install dependancies 

    pip install -r requirements.txt


4. Configure Enviroment Variables 

    -- Windows -- 
    copy .env.example .env

    -- Mac / Linux --
    cp .env.example .env


5. Initialise the seeded data

    python manage.py migrate
    python manage.py loaddata seeded_data.json ####IF FILE NAME IS seeded_data     

6. Run the Museum 

    python manage.py runserver 

Once the server is running, open browser and go to [http://127.0.0.1:8000/] (http://127.0.0.1:8000/)


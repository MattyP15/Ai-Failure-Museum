#!/bin/bash
cd "$(dirname "$0")" 


echo "Starting the Museum"

if [ ! -f .env ]; then
    echo -n "Enter a secure, random key to use as your museum key"
    read user_key

    echo "SECRET_KEY=$user_key" > .env
    echo "DEBUG=True" >> .env
else echo ".env already exists"
fi 

cd "./4_code/djangoCode"

## checking for virtual enviroment, if not then create one
if [ ! -d ".venv" ]; then 
    python3 -m venv .venv
fi

source .venv/bin/activate
pip install -r requirements.txt
## adding seeded data
python3 manage.py migrate 

python3 manage.py loaddata seeded_data.json


echo "Opening browser at http://127.0.0.1:8000/"

python3 manage.py runserver


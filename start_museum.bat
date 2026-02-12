
echo "Starting the Museum"

:: checking for//creating .env 
if not exist .env (
    set /p USER_KEY="Enter a secure, random key to use as your museum key"
    echo SECRET_KEY=%USER_KEY& > .env
    echo DEBUG=True >> .env
)
else ( echo (".env already exists")
)



:: checking for venv, create if missing
if not exist .venv (
    python -m venv .venv
)

:: activate venv
call .venv\Scripts\activate 

pip install -r requirements.txt

:: seeded database setup
python manage.py migrate 
python manage.py loaddata sead_data.json 

:: open browser, run server

echo "Opening browser at http://127.0.0.1:8000/"

start http://127.0.0.1:8000/ 
python manage.py runserver
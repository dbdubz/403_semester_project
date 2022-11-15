# 403_semester_project
Team 3-14 IS 403 Project F2022

Project repository for our restaurant webapp for 403.

SETUP:

1. In terminal do cd restaurants (if not in         restaurants already)

2. In terminal, run pip install python-dotenv

3. In restaurants app, create .env file (this allows for secure storing of keys and passwords... yes this one is public so it doesn't help, but it is good to do overall)

4. In .env put...
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-z*+@99kt&mc4)e0l&i_o(mr#%hut%_a(mbds7@0nbc+_sha$*n'
    db_password = Your password

5. In terminal run...
    pip install psycopg2
    pip install Pillow
    python manage.py makemigrations restaurants
    python manage.py sqlmigrate restaurants 0001
    python manage.py runserver
#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn poll.wsgi:application --bind 0.0.0.0:8080
web: gunicorn poll.wsgi --log-file -
web: python manage.py collectstatic --noinput && gunicorn poll.wsgi:application
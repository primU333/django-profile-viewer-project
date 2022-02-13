web: gunicorn django_profile_viewer.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

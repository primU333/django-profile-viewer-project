web: gunicorn django_profile/django_profile_viewer/wsgi.py:application --log-file - --log-level debug
heroku ps:scale web=1
python manage.py migrate

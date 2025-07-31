web: gunicorn jobportal.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate && python create_production_data.py && python manage.py collectstatic --noinput

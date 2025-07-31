web: python manage.py collectstatic --noinput && python manage.py migrate && gunicorn jobportal.wsgi:application --bind 0.0.0.0:$PORT
release: python create_production_data.py

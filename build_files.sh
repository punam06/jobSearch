#!/bin/bash

# Build script for Vercel
pip install -r requirements.txt

python manage.py collectstatic --noinput --clear

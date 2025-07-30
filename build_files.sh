#!/bin/bash

# Build script for Vercel
echo "BUILD_START"

pip3 install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD_END"

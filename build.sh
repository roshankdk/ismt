#!/usr/bin/env bash
# Build script for the Render test/dev deployment
set -o errexit

pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo

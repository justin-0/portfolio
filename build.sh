#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install -r requirements.txt

mkdir -p staticfiles
python manage.py collectstatic --no-input --clear
python manage.py migrate --run-syncdb
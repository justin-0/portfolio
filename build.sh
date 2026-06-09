#!/usr/bin/env bash
# exit on error
set -o errexit
python -m pip install --upgrade pip
pip install -r requirements.txt
mkdir -p staticfiles
python manage.py collectstatic --no-input --clear
python manage.py migrate --run-syncdb
echo "from django.contrib.auth import get_user_model; U = get_user_model(); U.objects.filter(username='admin').exists() or U.objects.create_superuser('admin', 'justion001james@gmail.com', 'admin123')" | python manage.py shell

#!/usr/bin/env bash

# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
python manage.py makemigrations
python manage.py migrate
python manage.py initadmin
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
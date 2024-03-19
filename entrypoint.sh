#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate

if [$l == 'gunicorn']; then

    exec gunicorn store_manage.wsgi:application -b 0.0.0.0:8000

else

    exec python manage.py runserver 0.0.0.0:8000

fi
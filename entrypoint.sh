#!/bin/bash
#Had too much problems with the database
set -e

echo "Running migrations..."
python store_manage/manage.py migrate
gunicorn store_manage.wsgi:application --bind 0.0.0.0:8000
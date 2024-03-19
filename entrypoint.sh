#!/bin/bash
#Had too much problems with the database
set -e

echo "Running migrations..."
python store_manage/manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn store_manage.wsgi:application -b 0.0.0.0:8000
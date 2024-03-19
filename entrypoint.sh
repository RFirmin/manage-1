#!/bin/bash
#Had too much problems with the database
set -e

python store_manage/manage.py migrate

if [ "$l" == "gunicorn" ]; then
    exec gunicorn store_manage.wsgi:application -b 0.0.0.0:8000
else
    exec python store_manage/manage.py runserver 0.0.0.0:8000
fi
#!/bin/bash
#Had too much problems with the database
set -e

echo "Running migrations..."
python store_manage/manage.py migrate
python store_manage/manage.py runserver
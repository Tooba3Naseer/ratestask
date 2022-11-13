#!/usr/bin/env bash

echo "################ start server ################"
python manage.py collectstatic --no-input --clear
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
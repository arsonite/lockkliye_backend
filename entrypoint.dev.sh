#!/bin/bash

if [ "$DATABASE" = "postgres" ]; then
    echo "Waiting for PostgreSQL ..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started!"
fi

# python manage.py flush --no-input
python manage.py makemigrations notes --noinput
python manage.py makemigrations server --noinput
python manage.py makemigrations workbench --noinput
python manage.py migrate --noinput

exec "$@"
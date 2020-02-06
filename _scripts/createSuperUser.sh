#!/bin/sh

docker-compose -f ../docker-compose.dev.yml exec database_test python manage.py createsuperuser
@ECHO OFF

docker-compose -f ..\docker-compose.dev.yml exec database_test python manage.py makemigrations database --noinput
docker-compose -f ..\docker-compose.dev.yml exec database_test python manage.py migrate --noinput
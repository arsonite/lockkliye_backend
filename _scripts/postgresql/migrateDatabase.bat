:: Turns off verbose-messages in command prompt
@ECHO OFF

:: TODO: Write a generalized script to migrate the content of the database
:: docker-compose -f ..\docker-compose.dev.yml exec database_test python manage.py makemigrations testapp --noinput
:: docker-compose -f ..\docker-compose.dev.yml exec database_test python manage.py migrate --noinput
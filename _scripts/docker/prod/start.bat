:: Turns off verbose-messages in command prompt
@ECHO OFF

:: Runs network creation script and starts the container with the custom file flag -f
CALL ..\createNetwork.bat
docker-compose -f ..\..\..\docker-compose.prod.yml up
@ECHO OFF
SETLOCAL EnableDelayedExpansion

docker network create VisionService
ECHO You can ignore warnings regarding an existing VisionService-Network
docker-compose -f ..\..\..\docker-compose.prod.yml build
docker-compose -f ..\..\..\docker-compose.prod.yml up -d
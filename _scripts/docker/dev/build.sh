#!/bin/sh

docker network create VisionService
docker-compose -f ../../../docker-compose.dev.yml build
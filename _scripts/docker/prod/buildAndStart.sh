#!/bin/sh

# Builds and starts the container with the custom file flag -f
sh build.sh
docker-compose -f ../../../docker-compose.prod.yml up
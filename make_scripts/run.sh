#!/usr/bin/env bash

SPINNER_IP=`cat src/settings.py | grep SPINNER_IP | cut -d "=" -f2 | cut -d "\"" -f2`
SPINNER_PORT=`cat src/settings.py | grep SPINNER_PORT | cut -d "=" -f2 | cut -d " " -f2`

python3 src/manage.py runserver ${SPINNER_IP}:${SPINNER_PORT}
#!/bin/bash

# Seed generation queue workers.
for (( i=1; i<=$QUEUE_WORKERS; i++ ))
do
   python manage.py db_worker --queue-name seeds &
done

# Web server.
gunicorn smrpg_web_randomizer.wsgi:application --bind 0.0.0.0:8000 --timeout 3600 -w $GUNICORN_WORKERS

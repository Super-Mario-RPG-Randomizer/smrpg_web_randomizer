#!/bin/bash

# Seed generation queue workers.
for (( i=1; i<=$QUEUE_WORKERS; i++ ))
do
   python manage.py db_worker --queue-name seeds &
done

# Web server.
uvicorn --reload --host 0.0.0.0 --port 8000 smrpg_web_randomizer.asgi:application

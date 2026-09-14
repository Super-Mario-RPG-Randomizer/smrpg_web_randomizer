#!/bin/bash

# Seed generation queue workers.
for (( i=1; i<=$QUEUE_WORKERS; i++ ))
do
   python manage.py db_worker --queue-name seeds &
done

# Web server.
python manage.py runserver 0.0.0.0:8000

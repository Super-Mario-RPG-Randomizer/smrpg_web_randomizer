#!/bin/bash

# Send SIGINT for queue workers.
for pid in $(ps -aux | grep 'db_worker' | grep -v grep | awk '{print $2}');
do
  kill -3 $pid
done

# Send regular exit code for web server.
for pid in $(ps -aux | grep 'runserver' | grep -v grep | awk '{print $2}');
do
  kill $pid
done

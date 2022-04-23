#!/bin/sh

python /app/app/run_server.py & sleep 5 && python /app/app/client.py

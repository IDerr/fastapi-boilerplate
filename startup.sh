#!/bin/bash
# Wait for DB
while ! timeout 20 bash -c "echo > /dev/tcp/db/5432"; do   
  sleep 1
done

prisma migrate dev && gunicorn --bind 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker app.server:app --reload
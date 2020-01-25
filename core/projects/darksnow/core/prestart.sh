#! /usr/bin/env bash

echo 'starting docker service'

#service docker start

echo 'starting DB'
python3 -m app.app.db.dbinit

echo 'starting server'
uvicorn app.app.main:app --host 0.0.0.0 --port 3000
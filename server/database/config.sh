#!/bin/bash
# set -e

python3 manage.py makemigrations
python3 manage.py migrate

# /etc/init.d/postgresql start
# sleep 5
# psql -f create_fixtures.sql    
# /etc/init.d/postgresql stop

"$@"
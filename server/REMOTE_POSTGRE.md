`sudo apt update`

`apt install postgresql postgresql-contrib`

`update-rc.d postgresql enable`

`service postgresql start`

`cd ../etc/postgresql/[10]/main`

## Edit pg_hba.conf

Add the following to the last paragragh:

`host all  all  [MY_IP_ADRESS]/24   trust`

_P.S. You might need to comment out the lines bove this one in that section._

## Edit postgresql.conf

Uncomment this line and add a star `listen_addresses = '*'`

`service postgresql restart`

Configure as required in PGADMIN.

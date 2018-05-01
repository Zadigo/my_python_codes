`sudo apt update`

`apt install postgresql postgresql-contrib`

`update-rc.d postgresql enable`

`service postgresql start`

`cd ../etc/postgresql/9.5/main`

Edit pg_hba.conf with the following:

`host all  all  0.0.0.0/0   trust`

Edit postgresql.conf:

`listen_addresses = '*'`

`service postgresql restart`

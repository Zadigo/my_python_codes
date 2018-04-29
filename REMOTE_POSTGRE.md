sudo apt update

apt install postgresql postgresql-contrib

update-rc.d postgresql enable

service postgresql startcd ../etc/postgresql/9.5/main

edit pg_hba.conf:   all  all  (YOUR IP ADDRESS)/32   trust

edit postgresql.conf:  listen_addresses = '*' 

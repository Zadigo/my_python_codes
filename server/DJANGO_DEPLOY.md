## UPDATE UBUNTU

`sudo apt-get update`
  
`sudo apt-get upgrade`

## INSTALL OTHER PACKAGES
  
`apt install tree`
  
`apt-get install fail2ban`

`sudo apt-get install htop`

## INSTALL PYTHON 3 (OPTIONAL)

`sudo apt-get install python-pip` or `sudo apt-get install python3-pip`

And, eventually pip : `apt install python-pip` ??????

## INSTALL NGINX (OPTIONAL - IF NOT PRESENT)

[https://docs.nginx.com/nginx/admin-guide/web-server/web-server/]

`sudo apt-get install nginx`

To check if NGINX is on the firewall do `sudo ufw app list`.

If not, then `sudo apt-get install nginx` and check again with `sudo ufw app list`.

You can now verify that Nginx is running by going on the IP address of the server where you should see the default page.

__NOTE:__ You might have to activate the firewall with `sudo ufw enable` and then check with `sudo ufw status`.

## INSTALL POSTGRESQL (OPTIONAL)
  
`sudo apt-get install postgresql postgresql-contrib`

Now, we can manage our database with a remote access through  PG ADMIN 4. See installation process
in __remote postgres__ github file.

## INSTALL AND CREATE VIRTUAL ENVIRONMENT

`pip3 install virtualenv`

`virtualenv -p python3 [environment_name]`

_You can create it in a special directory e.g. /home/ubuntu/virtualenvs/your-env_

### Clone repository

`git clone [repository]`

Activate the virtualenv e.g. source /home/ubuntu/virtualenvs/[your-env]/bin/activate to install the
requirements file and migrate the database.

### Collect static

Change the following lines in applications settings in order to collect all the static files
in the static directory specified in static root:

`STATIC_ROOT = '/home/ubuntu/[folder_name]/static/'`

`STATIC_URL = '/static/'`

And run `python3 manage.py collectstatic`.

### Testing the project on the server

 Run `sudo ufw allow 8000` to allow the :8000 port then `python3 manage.py runserver 0.0.0.0:8000`.
 
 Go to [SERVER_IP_ADRESS]:8000 to see the website in action.

### Testing with Gunicorn

If not done already, install gunicorn in environment `pip install gunicorn` and test that it
can run the project with `gunicorn [project_name].wsgi:application`.

Once done, run `gunicorn --bind 0.0.0.0:8000 [project_name].wsgi:application` to bind the project to the that same port that we were on with python manage.py above. Normally the website should show again using gunicorn.

Now deactivate the virtual environment

## CREATING THE SCRIPT TO RUN GUNICORN AUTOMATICALLY

Install supervisor `sudo apt-get install supervisor`.

Create a script that will run gunicorn with `nano home/ubuntu/gunicorn_start.bash`, then write the following:


```
#!/bin/bash

NAME="[project_name]"                                                    # Project name
DJANGODIR=/home/ubuntu/[folder_name]/[repository_name]/[project_folder]  # Project directory
SOCKFILE=/home/ubuntu/[folder_name]/[reposi_name]/[project_folder]/[project]/gunicorn.sock  # Path to the UNIX socket
USER=ubuntu                                                              # The user to run as
GROUP=ubuntu                                                             # The group to run as
NUM_WORKERS=3                                                            # How many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=[project_name].settings                           # which settings file should Django use
DJANGO_WSGI_MODULE=[project_name].wsgi                                   # WSGI module name

echo "Starting $NAME as `Ubuntu`"

# Activate the virtual environment
cd $DJANGODIR
source ../../../virtualenvs/env/bin/activate                             # Check configuration with ls -la /path/
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor
# should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-
```

Make it executable with `sudo chmod u+x gunicorn_start.bash` and then test the script with `./gunicorn_start.bash`.

## CREATING THE MONITORING FILE

Create a file to monitor gunicorn `nano /etc/supervisor/conf.d/[project_name].conf` and write the following:

```
[program:project_name]
command = /home/ubuntu/gunicorn_start.bash                            ; Command to start app
user = root                                                           ; User to run as
stdout_logfile = /var/log/gunicorn/gunicorn.out.log                   ; Where to write log messages
redirect_stderr = true                                                ; Save stderr in the same log
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8 
```

From the specified path indicated in `stderr_logfile`, create the gunicorn log directory `mkdir var/log/gunicorn` to receive the log error files.

__NOTE :__ When setting the user, make sure it can access the specified path. If it can't, watch for errors related to fatal and check which user-group has access to the file.

__NOTE :__ It is is important to check all the paths by running `ls -la [path]` on each of them.

### Update Supervisor

http://supervisord.org/running.html

Use `supervisorctl reread`, `supervisorctl update` then `supervisorctl status` to update with the new settings (can be used with _sudo_).

Test also with `spervisorctl start [project]`.

Reread should output _available_, update _added process group_ and status __.

Reload NGINX `service nginx reload` and then eventually `service nginx status`.

If errors, use supervisorctl reload to reload supervisor.

## MONITORING NGINX WITH REAL TIME REQUESTS
`tail -f /var/log/nginx/error.log`

You might get some errors _.sock failed (2: No such file or directory)_ if the files do not have correct permissions or _.sock failed (13: Permission denied)._

To get the non-errors `tail -f /var/log/nginx/access.log`

## NGINX
### Create file in sites available
`sudo nano etc/nginx/sites-available/[choose_a_name]` and delete default site `rm -v default` and copy these lines into the file:

```
proxy_cache_path /home/ubuntu/tmp/cache levels=1:2 keys_zone=cache:10m
                                        max_size=100m inactive=60m use_temp_path=off;

server {
    listen 80;
    server_name [server_name];
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root home/ubuntu/[folder_name]/static;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/[folder_name]/[repository_name]/[project_name].sock;
    }
    
    # caching
    location ~* \.(css|js|gif|jpe?g|png)$ {
        expires 168h;
        add_header Pragma public;
        add_header Cache-Control "public, must-revalidate, proxy-revalidate";
    }
}
```

__NOTE :__ Check that proxy_pass has the good path with ls -la

### Create link in sites enabled

CD to sites-enabled and `sudo ln -s ../sites-available/[choose_a_name]`.

Test NGINX configuration with `sudo service nginx configtest` then start it with `sudo service nginx start`.


### Finally check permissions

[https://en.wikipedia.org/wiki/Chmod]

Permissions have to be correct in order for NGINX to access the folders set in the conf file and fix the errors above.

If not, gives error __502 Bad Gateway__ and error __13 permission denied__ in `tail /var/log/gunicorn/gunicorn.out.log`.

To check permissions to path use `ls -la /home/ubuntu/[folder_name]`. Group should be rwx or r-x.

First, create a group `sudo groupadd varwwwusers`

Add NGINX "www-data" user to the group: `sudo adduser www-data varwwwusers`

Change the folder's group to the varwwwusers: `sudo chgrp -R varwwwusers /home/ubuntu/[folder_name]`

Finally, change the access mode: `sudo chmod -R 760 /home/ubuntu/[folder_name]` (or 770).

## DEBUGGING COMMANDS

See all ports `netstat -ntlp | grep LISTEN`

Default NGINX page `/usr/share/nginx/html` or `/var/www/html/index.nginx-debian.html`

Alt to check that path has correct permissions `sudo -u www-data stat /home/ubuntu/site1` or ls -la [path]

Gunicorn log data: `sudo -u www-data stat /home/ubuntu/site1`

Watching Gunicorn logs : tail -f /var/log/nginx/error.log

supervisorctl tail -5000 procname stderr

To inspect all processes: htop or ps -A

To read the log error files e.g. `tail var/log/gunicorn/file.log`
  
## COMMON ERRORS

ERROR (no such process) or No config updates to processes = check gunicorn file and that it ends with .conf

ERROR in gunicorn, bash file or NGINX conf are generally related to bad paths.

__WEBSITE AUTHORIZATION:__ NGINX is not on firewall

__INTERNAL SERVER ERROR:__ Restart your server















nano /etc/supervisor/conf.d/ilang.conf
tail var/log/supervisor/supervisord.log





  

















### Create user (optional):
`sudo -u postgres createuser --interactive`
  
### Create database:
`createdb _database_name_` or `createdb --owner user_name database_name`

You can start the database : /usr/lib/postgresql/10/bin/pg_ctl -D /var/lib/postgresql/10/main -l logfile start

## CREATE/START VIRTUALENV, GUNICORN
Create virtual environment `virtualenv -p python3 [environment_name]`.

If virtual envvironment does not exist yet, install with `pip install virtualenv`.

Activate it with `source [enviconment_name]/bin/activate` and install required packages with `pip install -r requirements.txt`.

Once done, install gunicorn in environment `pip install gunicorn` and test with `gunicorn [project_name].wsgi:application`.

Then run `gunicorn --bind 0.0.0.0:8000 [project_name].wsgi:application`

If no errors, create a file to monitor gunicorn with supervisor `nano /etc/supervisor/conf.d/gunicorn.conf` and write the following:

```
[program:gunicorn] 
directory=/home/ubuntu/[folder_name] 
command=/root/home/[virtualenv_name]/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/[folder_name]/[repository]/[project_name].sock [project_name].wsgi:application 
autostart=true 
autorestart=true 
stderr_logfile=/var/log/gunicorn/gunicorn.out.log 
stdout_logfile=/var/log/gunicorn/gunicorn.err.log 
user=root 
group=www-data 
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8 

[group:guni] 
programs:gunicorn
```



OTHER GUNI CONF without the script

[program:gunicorn] 
directory=/home/ubuntu/[folder_name] 
command=/root/home/[virtualenv_name]/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/[folder_name]/[repository]/[project_name].sock [project_name].wsgi:application 
autostart=true 
autorestart=true 
stderr_logfile=/var/log/gunicorn/gunicorn.out.log 
stdout_logfile=/var/log/gunicorn/gunicorn.err.log 
user=root 
group=www-data 
environment=LANG=en_US.UTF-8,LC_ALL=en_US.UTF-8 

[group:guni] 
programs:gunicorn
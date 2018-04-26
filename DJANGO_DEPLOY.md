## UPDATE UBUNTU
`sudo apt-get update`
  
`sudo apt-get upgrade`
  
`apt  install tree`
  
`apt-get install fail2ban`

`sudo apt-get install supervisor`

## INSTALL NGINX (OPTIONAL - IF PRESENT)
`sudo apt-get install nginx`

### CREATE FILE IN SITES AVAILABLE
`sudo nano etc/nginx/sites-available/_site_name_`
  
Copy these lines:

```
server {
    listen 80;
    server_name 51.38.34.10;
    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root root/site1/octo-carnival/site1/;
    }
    location / {
        include proxy_params;
        # proxy_pass http://unix:/root/site1/octo-carnival/site1/site1.sock;
        proxy_pass http://51.38.34.10:8000;
    }
}
```
Then `supervisorctl reread`, `supervisorctl update` then `supervisorctl status`.

### CREATE FILE IN SITES ENABLED
Enter in sites-enabled `cd /etc/nginx/sites-enabled` to create file that points towards sites-available `sudo ln -s ../sites-available/`.
  
Test that nginx is allowed on firewall `sudo ufw app list` and reload `service nginx reload`.

## INSTALL PYTHON 3 (OPTIONAL)
`sudo apt-get install python-pip` or  `sudo apt-get install python3-pip`
  
## INSTALL POSTGRESQL (OPTIONAL)
`sudo apt-get update`
  
`sudo apt-get install postgresql postgresql-contrib`

Create user (optional):
`sudo -u postgres createuser --interactive`
  
Create database:
`createdb _database_name_` or `createdb --owner user_name database_name`

## CLONE, CREATE/START VIRTUALENV, GUNICORN
Once app is cloned from git, create virtualenv `virtualenv -p python3 environment_name`.

Activate it with `source environment_name/bin/activate` and install required packages `pip install -r requirements.txt`. Then `pip install gunicorn` and test with `gunicorn project_name.wsgi:application`.

then `gunicorn --bind 0.0.0.0:8000 project_name.wsgi:application`

create to monitor gunicorn with supervisor `nano /etc/supervisor/conf.d/gunicorn.conf` an write:

```
[program:gunicorn] 
directory=/home/django/app-django/app 
command=/root/.virtualenvs/virtual-env-name/bin/gunicorn --workers 3 --bind unix:/home/django/app-django/app/app.sock app.wsgi:application 
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

## CONFIGURE COLLECT STATIC & RUN
Change in applications settings:

`STATIC_ROOT = '/opt/project_name/static/'`

STATIC_URL = '/static/'

`python3 manage.py collectstatic`


monitoring NGINX real time requests

tail -f /var/log/nginx/error.log

non-errors
tail -f /var/log/nginx/access.log

  

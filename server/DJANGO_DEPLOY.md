## UPDATE UBUNTU
`sudo apt-get update`
  
`sudo apt-get upgrade`
  
`apt  install tree`
  
`apt-get install fail2ban`

`sudo apt-get install supervisor`

## INSTALL NGINX (OPTIONAL - IF NOT PRESENT)

[https://docs.nginx.com/nginx/admin-guide/web-server/web-server/]

`sudo apt-get install nginx` and check that it is allowed on firewall `sudo ufw app list`

### CREATE FILE IN SITES AVAILABLE
`sudo nano etc/nginx/sites-available/[app_name]` and delete default site `rm -v default`
  
Copy these lines into the file:

```
server {
    listen 80;
    server_name [server_name];
    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        root opt/[project_name]/static;
    }
    
    location / {
        include proxy_params;
        proxy_pass http://unix:/root/[folder_name]/[repository_name]/[app_name].sock;
    }
    
    # caching
    location ~* \.(css|js|gif|jpe?g|png)$ {
        expires 168h;
        add_header Pragma public;
        add_header Cache-Control "public, must-revalidate, proxy-revalidate";
    }
}
```
### CREATE FILE IN SITES ENABLED
Enter in sites-enabled `cd /etc/nginx/sites-enabled` to create file that points towards sites-available `sudo ln -s ../sites-available/[choose_a_name]`.

## Update Supervisor

http://supervisord.org/running.html

Use `supervisorctl reread`, `supervisorctl update` then `supervisorctl status` to update with the new settings.

Reload NGINX `service nginx reload` and then eventually `service nginx status`.

## INSTALL PYTHON 3 (OPTIONAL)
`sudo apt-get install python-pip` or  `sudo apt-get install python3-pip`
  
## INSTALL POSTGRESQL (OPTIONAL)
`sudo apt-get update`
  
`sudo apt-get install postgresql postgresql-contrib`

### Create user (optional):
`sudo -u postgres createuser --interactive`
  
### Create database:
`createdb _database_name_` or `createdb --owner user_name database_name`

## CREATE/START VIRTUALENV, GUNICORN
Create virtual environment `virtualenv -p python3 [environment_name]`.

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

## CONFIGURE COLLECT STATIC & RUN
Change the following lines in applications settings in order to collect all the static files:

`STATIC_ROOT = '/opt/[project_name]/static/'`

`STATIC_URL = '/static/'`

And run `python3 manage.py collectstatic` to copy static files to `opt/project_name/static`


## Monitoring NGINX real time requests
`tail -f /var/log/nginx/error.log`

non-errors
`tail -f /var/log/nginx/access.log`

## Finally check permissions
Permissions have to be correct in order for NGINX to access the folders set in the conf file. If not, gives error __502 Bad Gateway__ and error __13 permission denied__ in `nano /var/log/gunicorn/gunicorn.out.log`.

To check permissions to path use `ls -la /home/ubuntu/[folder_name]`.

First, create a group
`sudo groupadd varwwwusers`

Add user to the group. Generally NGINX is `www-data`
`sudo adduser www-data varwwwusers`

Change the folder's group to the wwvarusers:
`sudo chgrp -R varwwwusers /home/ubuntu/[folder_name]`

Finally, change the access mode:
`sudo chmod -R 760 /home/ubuntu/[folder_name]`

# DEBUGGING COMMANDS
See all ports `netstat -ntlp | grep LISTEN`

Default NGINX page `/usr/share/nginx/html` or `/var/www/html/index.nginx-debian.html`

Alt to check that path has correct permissions `sudo -u www-data stat /root/site1`

Gunicorn log data: `sudo -u www-data stat /root/site1`
  

## UPDATE UBUNTU
  > sudo apt-get update
  
  > sudo apt-get upgrade
  
  > apt  install tree
  
  > apt-get install fail2ban

## INSTALL NGINX
  > sudo apt-get install nginx

### EDIT FILES SITES AVAILABLE
  > sudo nano etc/nginx/sites-available/`site_name`
  
Copy these lines:

```
server {
    server_name yourdomainorip.com;

    access_log off;

    location /static/ {
        alias /opt/myenv/static/;
    }

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header X-Forwarded-Host $server_name;
        proxy_set_header X-Real-IP $remote_addr;
        add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
    }
}
```
  
Enter in sites-enabled to create point to that file:
  > cd /etc/nginx/sites-enabled
  
  > sudo ln -s ../sites-available/
  
Test that nginx is allowed on firewall
  > sudo ufw app list
  
## INSTALL PYTHON 3 (OPTIONAL)
  > sudo apt-get install python-pip // sudo apt-get install python3-pip
  
## INSTALL POSTGRESQL (OPTIONAL)
  > sudo apt-get update
  
  > sudo apt-get install postgresql postgresql-contrib

Create user (optional):
  > sudo -u postgres createuser --interactive
  
Create database:
  > createdb `database_name`

Or:
  > createdb --owner `user_name` `database_name`


  
  

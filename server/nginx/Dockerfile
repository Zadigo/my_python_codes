FROM nginx

# Remove sites default
# RUN rm /etc/nginx/sites-available/default

# Copy NGINX configuration file
COPY nginx.conf /etc/nginx/nginx.conf
# Create site configuration in sites-available
COPY site1 /etc/nginx/sites-available

RUN mkdir /etc/nginx/sites-enabled
RUN ln -s /etc/nginx/sites-available/site1 /etc/nginx/sites-enabled/site1

# RUN service nginx configtest
RUN ls -a /etc/nginx/sites-available

EXPOSE 8080

# Nginx start
CMD ["nginx", "-g", "daemon off;"]
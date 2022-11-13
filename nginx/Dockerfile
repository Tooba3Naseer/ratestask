# Base image
FROM nginx:1.21.0-alpine

# 777 permissions to a file means that it will be readable, writable and executable by all users 
RUN chmod 777 /etc/nginx/conf.d/default.conf
# Remove the default config file for nginx
RUN rm /etc/nginx/conf.d/default.conf
# Copy our nginx.conf file into the /etc/nginx/conf.d directory
COPY nginx.conf /etc/nginx/conf.d

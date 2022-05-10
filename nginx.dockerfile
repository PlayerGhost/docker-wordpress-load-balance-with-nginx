FROM nginx:1.19.0

COPY /nginx/nginx.conf /etc/nginx/nginx.conf
# ADD /nginx/nginx.conf /etc/nginx/nginx.conf

# RUN /etc/init.d/nginx start
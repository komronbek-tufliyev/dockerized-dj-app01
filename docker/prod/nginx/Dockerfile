FROM nginx:1.21.1-alpine

# Add metatag to the image
LABEL dev.komronbek.author="Komronbek Tufliyev" \
        dev.komronbek.email="tufliyev@tuit.uz" \
        dev.komronbek.version="0.0.1" \
        dev.komronbek.description="This is a Dockerfile for Nginx image" 

# Set environment variables
RUN rm /etc/nginx/conf.d/default.conf

# Copy the nginx configuration file
COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d


# Use an official Python runtime as a parent image
FROM python:3.9.6-alpine

# Set the working directory to /app
WORKDIR /usr/src/app

# RUN apt update
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# COPY requirements.txt
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY the project 
COPY . .

# RUN the project
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000

# CMD specifcies the command to execute to start the server running.
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"] 


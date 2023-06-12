# Use an official Python runtime as a parent image
FROM python:3.9.6-alpine

# Set the working directory to /app
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# COPY requirements.txt
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY the project 
COPY . .


FROM python:3.9.6-alpine3.14

LABEL Author="Komronbek"

ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV COLUMNS 143

WORKDIR /app

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev libpcap-dev postgresql-dev
# RUN apt-get update \
#     && apt-get install -y build-essential libpq-dev \
#     && rm -rf /var/lib/apt/lists/*


RUN 

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools


COPY requirements.txt /app

RUN pip install virtualenv
RUN virtualenv venv 
RUN echo "Installed and created virtual environment⛳"
RUN source venv/bin/activate
RUN echo "Successfully activated venv environment🔓"

RUN pip install -r requirements.txt
RUN echo "Installed all depencises🎉"

COPY . /app
RUN echo "Docker file ended"

# CMD ["python", "manage.py", "migrate"]



# EXPOSE 8000

# RUN python manage.py collectstatic --noinput
# # RUN python manage.py makemigrations
# RUN python manage.py migrate


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


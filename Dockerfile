FROM python:3.9.6-alpine3.14

LABEL Author="Komronbek"

ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# ENV COLUMNS 143


WORKDIR /app

RUN pip install --upgrade pip

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

# EXPOSE 8000

# RUN python manage.py collectstatic --noinput
# # RUN python manage.py makemigrations
# RUN python manage.py migrate


# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


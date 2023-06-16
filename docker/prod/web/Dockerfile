FROM python:3.9.6-alpine

# Set the working directory to /app
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# COPY requirements.txt
RUN pip install --upgrade pip

COPY . .

ENTRYPOINT [ "/home/app/docker/prod/entrypoint.sh" ]

ADD . /app

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "config.wsgi:application"]
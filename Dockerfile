# Use an official Python runtime as a parent image
FROM python:3.10.6

# Set the working directory to /app
WORKDIR /app

# COPY requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# COPY the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
# EXPOSE 80

# Run app.py when the container launches
CMD ["python", "main.py"]


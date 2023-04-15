# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app .

# Install any needed packages specified in requirements.txt
# RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install --upgrade pip --no-cache-dir
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Expose the port that the application will run on
EXPOSE 8000

# Run the command to start the application
CMD gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app

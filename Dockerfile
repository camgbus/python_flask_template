# Ubuntu container
FROM ubuntu:16.04

# Python 3.6 as parent image
FROM python:3.6-slim

# Inatall pip
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# Copy first requirements.txt to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install requirements in requirements.txt with pip
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available from utside the container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]

# docker build --tag=template .
# docker run -p 3000:80 template
# Open browser on http://localhost:3000/

# To remove everything: docker system prune -a --volumes
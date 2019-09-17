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

# Make port 80 available from outside the container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]

# To run locally:
# docker build --tag=template .
# docker run -p 3000:80 template
# Open browser on http://localhost:3000/

# To push image:
# Push: docker tag template <registry>.azurecr.io/<image_name>:v1.0.0
# Push: docker push <registry>.azurecr.io/<image_name>:v1.0.0
# On Azure console, have app listen to port 80

# To remove everything: docker system prune -a --volumes
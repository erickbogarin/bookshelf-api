# Pull base image
FROM python:3.6-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./compose/local/start /start
RUN pip install --upgrade pip
ADD . /code/
RUN pip install -Ur requirements/local.txt

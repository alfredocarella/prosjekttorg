# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Only to generate translation strings. Could be removed in production.
RUN apt update && apt install -y gettext

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project 
COPY . /code/

# Compile (new) translation strings
RUN python manage.py compilemessages

# Collect static files
RUN mkdir -p /code/staticfiles
RUN python manage.py collectstatic --noinput

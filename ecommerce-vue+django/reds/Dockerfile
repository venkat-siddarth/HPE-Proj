# FROM python:latest
# ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR .
# # COPY Requirements.txt .
# COPY . .
# RUN pip install -r Requirements.txt

# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR .
COPY Requirements.txt .
RUN pip install -r Requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8001
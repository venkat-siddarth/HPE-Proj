# syntax=docker/dockerfile:1
FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR .
# RUN cd
COPY Requirements.txt .
RUN pip install -r Requirements.txt
COPY . .
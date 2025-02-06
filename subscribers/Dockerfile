# Use an official Python image as the base image
FROM python:3.9-slim

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Copy your application code into the container
COPY /subscribers/subscriber.py /app/subscriber.py

# Install any necessary dependencies
RUN pip install pip --upgrade
RUN pip install redis

# Set the default command
CMD ["python", "/app/subscriber.py"]
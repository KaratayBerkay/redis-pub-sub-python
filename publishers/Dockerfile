# Use an official Python image as the base image
FROM python:3.9-slim

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Set the working directory
WORKDIR /app

# Copy your application code into the container
COPY /publishers/publisher.py /app/publisher.py
COPY /requirements.txt /app/requirements.txt

# Install any necessary dependencies
RUN pip install pip --upgrade
RUN pip install -r /app/requirements.txt --no-cache-dir

# Set the default command
CMD ["python", "/app/publisher.py"]

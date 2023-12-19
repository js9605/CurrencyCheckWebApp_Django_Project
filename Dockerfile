# Use an official Python runtime as a parent image
FROM python:3.11.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the entire project into the container at /app
COPY . /app/

# Expose the port that Django will run on
EXPOSE 8000

# Celery
RUN pip install celery[redis]

COPY currencycheckproject/celery.py /app/currencycheckproject/celery.py
COPY currencycheckproject/currencycheckapp/tasks/celery_tasks.py /app/currencycheckproject/currencycheckapp/tasks/celery_tasks.py

# Command to run on container start
CMD ["python", "currencycheckproject/manage.py", "runserver", "0.0.0.0:8000"]

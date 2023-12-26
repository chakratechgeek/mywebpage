# Use a Python base image with required Python version
FROM python:3.10

# Set working directory in the container
WORKDIR /root/django/app 

# Copy the local code to the container
COPY . /root/django/app 

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port used by Django (default is 8000)
EXPOSE 8000

# Define the command to start the Django server
#end
CMD ["python", "/root/django/app/manage.py", "runserver", "0.0.0.0:8000"]


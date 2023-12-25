# Use a base image with Python pre-installed
FROM python:3.9

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Expose the port that the Django app runs on
EXPOSE 8000


# Install Gunicorn
RUN pip install gunicorn

# Command to run the Django application using Gunicorn (replace 'yourapp' with your actual Django app name)
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "My_App.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

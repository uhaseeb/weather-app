# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Set the default command to run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use official Python image as the base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app's code
COPY . /app/

# Expose the Flask app's port
EXPOSE 5000

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV DATABASE_URL=postgresql://postgres:password@db:5432/mydatabase
# Run the Flask app
# use this command (instead of the one underneath) for auto-reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
# CMD ["flask", "--app", "app", "--debug", "run", "--host=0.0.0.0", "--port=5000"]

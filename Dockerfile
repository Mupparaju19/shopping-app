# Use a specific version of the Python image for consistency
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker cache during builds
COPY requirements.txt .

# Install the Python dependencies from the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code (excluding files mentioned in .dockerignore)
COPY . .

# Expose the port that the Flask app will run on
EXPOSE 5000

# Use a non-root user for security reasons
RUN adduser --disabled-password --gecos "" myuser
USER myuser

# Use Gunicorn for running the application in production
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]



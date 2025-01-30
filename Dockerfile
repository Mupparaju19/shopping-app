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
RUN adduser --disabled-password myuser
USER myuser

# Run the application with Flask (production servers like Gunicorn can be used for production)
CMD ["python", "app.py"]


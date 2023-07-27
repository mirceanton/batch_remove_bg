# Use the official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install the required dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script to the container's working directory
COPY removebg.py ./

# Run the image processing script when the container starts
ENTRYPOINT ["python", "-u", "removebg.py"]

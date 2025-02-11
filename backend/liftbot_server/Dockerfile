# Use an official lightweight Python image.
FROM python:3.10-slim

# Set the working directory in the container.
WORKDIR /app

# Copy the dependency list and install dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code.
COPY . .

# Copy the entrypoint script and ensure it is executable.
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set environment variable for configuration (can be overridden by docker-compose or CLI).
ENV APP_ENV=development

# Expose the port that your app listens on.
EXPOSE 5003

# Use the entrypoint script.
ENTRYPOINT ["/entrypoint.sh"]

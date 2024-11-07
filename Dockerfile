# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Install necessary system dependencies
RUN apt-get update && apt-get install -y \
    libodbc1 \
    unixodbc-dev \
    curl \
    gnupg2 \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code

# Install Python packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run CART_AZURE.py when the container launches
CMD ["python", "CART_AZURE.py"]

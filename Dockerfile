# Use an official Python runtime as the parent image
FROM python:3.9-slim

# Set the maintainer label
LABEL maintainer="rgeogriev@2zsrf2.onmicrosoft.com"

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Install libpcap for packet capture
RUN apt-get update && apt-get install -y libpcap-dev

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Grant permissions for the script to be executable
RUN chmod +x /app/src/sniffing/sniffer.py

# Set the default command to execute
# Here, we'll use the bash shell.
CMD [ "bash" ]

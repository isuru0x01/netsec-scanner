# Start with a Kali Linux base image
FROM ubuntu:22.04

# Update and install tools (e.g., nmap, sqlmap, and custom scripts)
RUN apt update && \
    apt install -y \
    nmap \
    sqlmap \
    python3-pip \
    && apt clean

# Add custom scripts to the container
COPY ./scripts /opt/my-tools

# Set working directory and environment variables
WORKDIR /opt/my-tools
ENV PYTHONPATH=/opt/my-tools

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Define entry point for the container
ENTRYPOINT ["python3", "scanner.py"]
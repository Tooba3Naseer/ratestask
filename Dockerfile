# Base image
FROM python:3.8.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the application code that is in current directory to the /ratestask directory of the container
COPY . ./ratestask

# Create an env variable and assign a value to it. We can access its value by using $ratestask
ENV ratestask=/ratestask

# WORKDIR instruction is used to set the working directory for all the subsequent Dockerfile instructions
WORKDIR $ratestask

# Install all the pacakges that are specified in requirements.txt
RUN pip install -r requirements.txt

# The EXPOSE instruction exposes the specified port and makes it available only for inter-container communication
EXPOSE 8000

# Run commands that are specified in entrypoint.sh file. These commands will run the server.
ENTRYPOINT ["/ratestask/entrypoint.sh"]
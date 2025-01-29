# Docker Vulnerability Demonstration with Flask

This project demonstrates a Docker API vulnerability using a Flask web application. The goal is to illustrate how insecure Docker APIs can be exploited to execute commands on a host machine and gain unauthorized access to sensitive information or services.

## Features

Docker API Exposure: A Flask app that exposes an insecure Docker API allowing remote execution of Docker commands.
Docker Command Injection: Allows users to execute Docker commands (e.g., ps, ps -a, inspect, exec, etc.) via a vulnerable endpoint.
Remote Command Execution: Test various Docker commands to exploit the exposed API and understand its potential risks.
No Authentication: No authentication or authorization is in place, making it vulnerable to unauthorized command execution.

## Prerequisites

1.Docker Desktop: Install Docker Desktop on your machine. Ensure that it is configured to expose the Docker Remote API without TLS (for testing purposes).
2.Expose Docker Remote API without TLS:
    -Go to Settings > General in Docker Desktop.
    -Enable the option: Expose daemon on tcp://localhost:2375 without TLS.
    -This will allow the Docker API to be accessed over HTTP on port 2375.
3.Verify the Docker Remote API: After configuring the settings, you can verify that the API is exposed correctly by running the following curl command:
```bash
curl http://localhost:2375/version
```
This should return the Docker version information if the API is exposed successfully.
4.Python: Install Python 3.12 or higher.

## Installation

1. Clone the Repository
```bash
git clone https://github.com/abarah/WEB_SERVICE.git
cd WEB_SERVICE
```
2.Build the Docker Image
```bash
docker build -t flask-docker-vulnerable .
```
3. Run the Docker Container
```bash
docker run -d -p 5000:5000 flask-docker-vulnerable
```
The application will now be running and accessible at http://127.0.0.1:5000.

## Usage

1. Access the Application
Open your browser and navigate to the following URL:
```bash
http://127.0.0.1:5000
```
2. Test the Vulnerability
You can now send POST requests with different Docker commands. Here are a few examples:

Example 1: List Running Containers
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"ps\"}" http://127.0.0.1:5000/vulnerable
```
Example 2: List All Containers (Including Stopped)
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"ps -a\"}" http://127.0.0.1:5000/vulnerable
```
Example 3: Inspect a Container
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"inspect <container_id>\"}" http://127.0.0.1:5000/vulnerable
```
Example 4: Execute a Command Inside a Container (e.g., bash)
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"exec <container_id> bash\"}" http://127.0.0.1:5000/vulnerable
```
Example 5: Stop a Container
```bash
curl -X POST -H "Content-Type: application/json" -d "{\"command\": \"stop <container_id>\"}" http://127.0.0.1:5000/vulnerable
```
You can replace <container_id> with actual IDs obtained from the ps command.

##Observing the Results
After sending requests, check the Flask server logs to observe the Docker commands being executed and their results. If the API is exposed to the public, an attacker could remotely execute arbitrary commands on the host machine, compromising security.








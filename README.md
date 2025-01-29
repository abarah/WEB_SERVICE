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
   

3. Build the Docker Image

4. Run the Docker Container







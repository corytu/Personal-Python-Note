# Docker

> Build, Manage and Secure Your Apps Anywhere. Your Way.

[Get Started with Docker](https://docs.docker.com/get-started/), especially Part 1 and Part 2, is a good starter before using Docker.

## Dockerfile

Here is the suggested format of Dockerfile:

```dockerfile
# Use an official Python runtime as a parent image
FROM python:<your_python_version>

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt individually to ensure the cached is used if there's no change in dependent packages
COPY requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container at the working directory, /app
COPY . /app

# Make port 7000 available to the world outside this container
# Always use port 7000 for ease of maintenance in the future
EXPOSE 7000

# Define a variable that users can pass at build-time to the builder
# Uncomment this line below when needed
# ARG <variable_name>

# Define environment variable
# Uncomment this line below when needed
# ENV <variable_name> <variable_content>

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### .dockerignore file

.dockerignore in Docker is like .gitignore in git.

> Before the docker CLI sends the context to the docker daemon, it looks for a file named `.dockerignore` in the root directory of the context. If this file exists, the CLI modifies the context to exclude files and directories that match patterns in it. This helps to avoid unnecessarily sending large or sensitive files and directories to the daemon and potentially adding them to images using `ADD` or `COPY`.

Some suggested that the syntax of .dockerignore is different from .gitignore (see references below), but such issue has not happened yet.

### References

- [Python runtimes](https://store.docker.com/images/python)
- [Use `COPY` instead of `ADD`](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/#add-or-copy)
- [Difference between `RUN` and `CMD` in a Dockerfile](https://stackoverflow.com/q/37461868/6666231)
- [Get environment variable value in Dockerfile](https://stackoverflow.com/q/19537645/6666231)
- [.dockerignore file](https://docs.docker.com/engine/reference/builder/#dockerignore-file)
- [Exclude a sub-directory with a .dockerignore file](https://stackoverflow.com/q/31181588/6666231)

## Build an Image with Dockerfile

1. Execute `sudo usermod -aG docker <your_username>` before doing anything related to `docker` commands in order to grant yourself permissions.
2. Execute `docker build -t <image_name> .` in the folder where Dockerfile exists.
  - If you have `ARG` set in Dockerfile, do `docker build --build-arg <set_arg>=<arg_value> -t <image_name> .`.
  - If you need to build an image without using cached resources (e.g. for debug purposes), do `docker build --no-cache -t <image_name> .`.

### References

- [Force docker for clean build of an image](https://stackoverflow.com/q/35594987/6666231)

## Run the App

Execute `docker run -p <mapped_port_of_server>:7000 <image_name>` to run the image.

- If you are running short-term foreground processes, do `docker run --rm -p <mapped_port_of_server>:7000 <image_name>`. __This is suggested to avoid generating many one-time containers while debugging.__
- If you'd like to run in the background, do `docker run -d -p <mapped_port_of_server>:7000 <image_name>`.

After running the app, you can test your app as per usual. Make sure your are sending requests to the `mapped_port_of_server` you configured.

### References

- [Clean up (--rm)](https://docs.docker.com/engine/reference/run/#clean-up---rm)
- [Detached vs foreground](https://docs.docker.com/engine/reference/run/#detached-vs-foreground)
# ATF Proof of concept

## Prerequisites

You will need to have a [modern version of `docker`](https://docs.docker.com/engine/release-notes/) 

## Usage
Build the image using the following command

```bash
$ docker build -t my-python-app .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 my-python-app
```

Get the docker container id 

```bash
$ docker ps
```

Verify the application

```bash
$ docker exec -it <container_id> /bin/bash
root@0490887928ef:/app#curl http://127.0.0.1:8081/getall
```

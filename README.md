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
$ docker run -it --rm --name my-running-app my-python-app
```

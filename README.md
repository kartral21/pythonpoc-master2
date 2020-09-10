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
## Running in Kubernetes

### Prerequisites
You must install and configure the following tools before moving forward

* kubectl(Kuberntes cluster)

### Deploy to Kubernetes

First verify your kubectl is configured. At the command line, type the following

```bash
$ kubectl version
```

Use kubectl to send the YAML file to Kubernetes by running the following command

```bash
$ kubectl apply -f deployment.yaml
```

You can see the pods are running if you execute the following command:

```bash
$ kubectl get pods
```
### Verify in Kubernetes

```bash
$ kubectl exec <your_pod_name> -it -- /bin/sh
$ curl http://127.0.0.1:8081/
Hello ATF!
```

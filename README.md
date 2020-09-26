## Introduction

This project is a demonstration of how to execute locust using docker, docker compose and minikube (kubernetes) using both its standalone and master/worker mode. It's heavly inspired in [this](https://github.com/karol-brejna-i/locust-experiments) repository and [this](https://github.com/karol-brejna-i/docker-locust).

## Dependencies

You need to have the three pieces installed: [docker](https://docs.docker.com/get-docker/), [docker compose](https://docs.docker.com/compose/install/) and [minikube](https://minikube.sigs.k8s.io/docs/start/). Then clone this repository and follow the execution scenarios:

    $ git clone https://github.com/gustavobgama/locust-k8s.git
    $ cd locust-k8s

## Execute locust with the standalone mode using docker

    $ docker run --name standalone --hostname standalone -e ATTACKED_HOST=https://computer-database.gatling.io -p 8089:8089 -d -v $(pwd):/locust gustavobgama/locust

So, access the locust [web interface](http://127.0.0.1:8089/), define the parameters for load test, execute and go along with the results. After the tests you can remove the container:

    $ docker rm -f standalone

You can also execute the load tests without the interface passing the command line [documented option](https://docs.locust.io/en/stable/configuration.html) in `LOCUST_OPTS`, for example:

    $ docker run --rm --name standalone --hostname standalone -e ATTACKED_HOST=https://computer-database.gatling.io -e "LOCUST_OPTS=--run-time=30s --spawn-rate=20 --users=200 --headless --only-summary" -p 8089:8089 -v $(pwd):/locust gustavobgama/locust

## Execute locust with the master/worker mode using docker compose

    $ docker-compose up --scale worker=4

The locust web interface will be available [here](http://127.0.0.1:8089/).

## Execute locust with the master/worker mode using minikube

For ultimate scalability and automation you can use the kubernetes to execute locust in master/worker mode, this setup is going to automatically activate or deactivate workers according to the load test scenario.

1. Start the cluster and enable some addons:

    $ minikube start
    $ minikube addons enable ingress
    $ minikube addons enable metrics-server

2. Configure the cluster and execute test:

    $ kubectl apply -f ./k8s
    $ minikube service master-load-balancer-service (open the locust web interface)

3. After tests you can remove the artifacts created:

    $ kubectl delete configmap,service,deployment,ingress --all
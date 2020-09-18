### Executar o modo standalone usando docker

$ docker run --rm --name standalone --hostname standalone -e ATTACKED_HOST=https://computer-database.gatling.io -p 8089:8089 -d -v $(pwd):/locust gustavobgama/locust

Então acesse: http://127.0.0.1:8089/ e execute o teste de carga

$ docker run --rm --name standalone --hostname standalone -e ATTACKED_HOST=https://computer-database.gatling.io -e "LOCUST_OPTS=--run-time=30s --spawn-rate=20 --users=200 --headless --only-summary" -p 8089:8089 -v $(pwd):/locust gustavobgama/locust

### Executar o modo master/workers usando docker e docker-compose

$ docker-compose up --scale worker=4

Então acesse: http://127.0.0.1:8089/ e execute o teste de carga

### Executar o modo master/worker usando kubernetes (minikube)

Para configurar o cluster:

    $ kubectl apply -f ./k8s
    $ minikube service master-load-balancer-service

Para remover o cluster basta executar:

    $ kubectl delete configmap,service,deployment,ingress --all

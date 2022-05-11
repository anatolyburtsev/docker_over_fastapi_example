### Build docker image

```commandline
docker build -t ml_on_prod . 
```

### Run docker image

```commandline
PORT=8088 # free local port
docker run -d -p ${PORT}:80 ml_on_prod
```

### Send request
```commandline
curl -d '{"name": "Alfred", "id": 10}' -H 'Content-Type: application/json' localhost:${PORT}/predict/
```

### Send health check 
```commandline
curl -v localhost:${PORT}/health
```

### push image to docker hub
```commandline
# go to hub.docker.com and create account first!
docker login
DOCKER_LOGIN="onotolemobile"
docker tag ml_on_prod ${DOCKER_LOGIN}/ml_on_prod
docker push ${DOCKER_LOGIN}/ml_on_prod 
```

### pull from docker hub and run
```commandline
docker pull ${DOCKER_LOGIN}/ml_on_prod
docker run -d -p ${PORT}:80 ${DOCKER_LOGIN}/ml_on_prod/ml_on_prod
```
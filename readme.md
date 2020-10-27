# Docker images

## Chronograf: Influxdb UI

`docker run -p 8888:8888 --network=iotstack_default chronograf --influxdb-url=http://influxdb:8086`

* Volume  
-v $PWD:/var/lib/chronograf

## Nginx

`docker run -p 8080:80 --network=iosetack_default nginx`


## Keycloack
docker run -itd -p 8081:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin ruifigueiredo/rpi-keycloak

# Docker images

## Chronograf: Influxdb UI

`docker run -p 8888:8888 --network=iotstack_default chronograf --influxdb-url=http://influxdb:8086`

* Volume  
-v $PWD:/var/lib/chronograf

## Nginx

`docker run -p 8080:80 --network=iosetack_default nginx`
## Prometheus
docker run -itd \
    -p 9090:9090 \
    -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus

docker run -itd \
    -p 9115:9115 \
    -v $(pwd)/blackbox.yml:/config/blackbox.yml \
    prom/blackbox-exporter

docker run -itd \
    -p 3000:3000 \
    -e GF_SECURITY_ADMIN_USER=notadmin \
    -e GF_SECURITY_ADMIN_PASSWORD=asdasd \
    grafana/grafana
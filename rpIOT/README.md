# Cosas hardcodeadas
services:
  influxdb:
    - influxdb.env usuarios y password
  grafana:
    - grafana.env usuario y auth github
    - datasources.yaml conexion al influxd

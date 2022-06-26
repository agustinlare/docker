# Minikube
Esto esta configurado para que todo se pueda exponer en una sola IP o HOST los root_url sean redirigidos a otro path.

## Addons
minikube addon enable ingress
minikube addons enable metallb
minikube addons configure metallb

## Kube-proxy CrashLoopBackOff
kubectl apply -f kube-proxy-configmap.yaml

## Prometheus & grafana
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/prometheus -f helm--prometheus.yaml
# If nginx=true
kubectl apply -f prometheus-ingress.yaml
# else
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-np
minikube service prometheus-server-np


helm repo add grafana https://grafana.github.io/helm-charts
# Cambiar la password
kubectl create -f grafana-secret.yaml
helm install grafana grafana/grafana -f helm-grafana.yaml
# If nginx=true
kubectl apply -f grafana-ingress.yaml
# else
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-np
minikube service grafana-np
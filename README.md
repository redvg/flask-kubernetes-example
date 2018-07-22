# Flask+Docker+Kubernetes

## To Build

```
git clone git@github.com:redvg/flask-on-k8s.git
cd flask-on-k8s

docker build . -t flask-on-k8s

docker run -d -p 5000:5000 flask-on-k8s

curl http://localhost:5000

```

## Deploying to Kubernetes

for v1 and v2\
for project id udemy-data-engineer-210920 (also see image in deployment.yaml)\
for port 5000

```
git clone https://github.com/redvg/flask-on-k8s
cd flask-on-k8s
docker build -t gcr.io/udemy-data-engineer-210920/flask-on-k8s:v1 .
docker images
gcloud docker -- push gcr.io/udemy-data-engineer-210920/flask-on-k8s:v1
gcloud container clusters create flask-cluster --zone europe-north1-a
gcloud compute instances list
kubectl run flask-on-k8s --image=gcr.io/udemy-data-engineer-210920/flask-on-k8s:v1 --port 5000
kubectl get pods
kubectl get deployment
kubectl expose deployment flask-on-k8s --name=flask-service --type=LoadBalancer --port 80 --target-port 5000
kubectl describe services
kubectl describe services flask-service
kubectl scale deployment flask-on-k8s --replicas=3
kubectl get deployment
kubectl get pods
docker build -t gcr.io/udemy-data-engineer-210920/flask-on-k8s:v2 .
docker images
gcloud docker -- push gcr.io/udemy-data-engineer-210920/flask-on-k8s:v2
kubectl get deployments
kubectl set image deployment/flask-on-k8s flask-on-k8s=gcr.io/udemy-data-engineer-210920/flask-on-k8s:v3
```

dont forget to release the bucket also

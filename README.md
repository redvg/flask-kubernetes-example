# Flask+Docker+Kubernetes

## To Build

```
git clone git@github.com:redvg/flask-on-k8s.git
cd flask-on-k8s

docker build . -t flask-on-k8s

docker run -d -p 5000:5000 flask-on-k8s

curl http://localhost:5000

```

## NB

note project ID for image in deployment.yaml

note port number at kubectl run & kubectl expose

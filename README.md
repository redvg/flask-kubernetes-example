# Flask+Docker+Kubernetes

## To Build

```
git clone git@github.com:theho/flask-kubernetes-example.git
cd flask-kubernetes-example

docker build . -t flask-kubernetes-example

docker run -d -p 5000:5000 flask-kubernetes-example

curl http://localhost:5000

```

## To Do

change project ID for image in deployment.yaml 

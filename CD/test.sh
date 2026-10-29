set -e

echo "Checking Minikube status..."

if ! minikube status; then
    echo "Minikube is not running. Starting Minikube..."
    minikube start --driver=docker
fi

echo "Updating Kubernetes context..."
minikube update-context

echo "Setting Kubernetes context..."
kubectl config use-context minikube

echo "Checking Kubernetes connectivity..."
kubectl cluster-info

echo "Checking Kubernetes nodes..."
kubectl get nodes --all-namespaces

echo "Waiting for Kubernetes nodes to be Ready..."
kubectl wait --for=condition=Ready nodes --all --timeout=120s

echo "Minikube cluster is ready!"
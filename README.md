# 🚀 Senior DevOps Lab: End to End Cloud-Native Pipeline

This project demonstrates a full-scale **CI/CD Lifecycle** and **Kubernetes Orchestration** environment. It moves a Python application from local development to a production-ready cluster using automated pipelines and professional ingress routing.

## 🏗️ Architecture Overview



1.  **CI (Continuous Integration):** GitHub Actions triggers on every push to `main`, builds a Docker image, and pushes it to **DockerHub**.
2.  **CD (Continuous Deployment):** Kubernetes pulls the latest image and performs a rolling update.
3.  **Ingress Routing:** An NGINX Ingress Controller manages external traffic, providing a professional entry point to the application.

---

## 🛠️ Tech Stack

* **Runtime:** Python (Flask/FastAPI)
* **Pipeline:** GitHub Actions
* **Registry:** DockerHub
* **Orchestrator:** Kubernetes (Kind)
* **Gateway:** NGINX Ingress Controller
* **Environment:** DevContainers (Infrastructure-as-Code workspace)

---

## 🚀 Getting Started

### 1. Prerequisites
This repo is designed to run in **GitHub Codespaces**. The `.devcontainer` configuration automatically installs `docker`, `kubectl`, and `kind`.

### 2. Spin up the Cluster
To recreate the production-grade environment with port mapping:
```bash
kind create cluster --name senior-lab --config kind-config.yaml

### 3.deploy the store stack
# Install Ingress Controller
kubectl apply -f [https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml](https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml)

# Wait for readiness
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=120s

# Deploy Application
kubectl create namespace production
kubectl apply -f k8s/deployment.yaml -n production
kubectl apply -f k8s/ingress.yaml -n production

Gemini said
This is the final touch that turns a collection of files into a Portfolio Project. A great README tells the story of your "Infrastructure as Code" journey.

Paste the following into your README.md file. I've designed it to highlight your mastery of GitHub Actions, DockerHub, and Kubernetes.

Markdown
# 🚀 Senior DevOps Lab: Cloud-Native Pipeline

This project demonstrates a full-scale **CI/CD Lifecycle** and **Kubernetes Orchestration** environment. It moves a Python application from local development to a production-ready cluster using automated pipelines and professional ingress routing.

## 🏗️ Architecture Overview



1.  **CI (Continuous Integration):** GitHub Actions triggers on every push to `main`, builds a Docker image, and pushes it to **DockerHub**.
2.  **CD (Continuous Deployment):** Kubernetes pulls the latest image and performs a rolling update.
3.  **Ingress Routing:** An NGINX Ingress Controller manages external traffic, providing a professional entry point to the application.

---

## 🛠️ Tech Stack

* **Runtime:** Python (Flask/FastAPI)
* **Pipeline:** GitHub Actions
* **Registry:** DockerHub
* **Orchestrator:** Kubernetes (Kind)
* **Gateway:** NGINX Ingress Controller
* **Environment:** DevContainers (Infrastructure-as-Code workspace)

---

## 🚀 Getting Started

### 1. Prerequisites
This repo is designed to run in **GitHub Codespaces**. The `.devcontainer` configuration automatically installs `docker`, `kubectl`, and `kind`.

### 2. Spin up the Cluster
To recreate the production-grade environment with port mapping:
```bash
kind create cluster --name senior-lab --config kind-config.yaml
3. Deploy the Stack
Bash
# Install Ingress Controller
kubectl apply -f [https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml](https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml)

# Wait for readiness
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=120s

# Deploy Application
kubectl create namespace production
kubectl apply -f k8s/deployment.yaml -n production
kubectl apply -f k8s/ingress.yaml -n production

📊 Scale & Monitoring
The application is configured to run with 5 replicas for high availability.

To observe the load balancer in action:

Bash
kubectl logs -f -l app=my-app -n production --max-log-requests=10

### 🏁 Your DevOps Journey is Complete
You have successfully:
1.  **Debugged** Python code.
2.  **Automated** a build pipeline.
3.  **Configured** a cloud registry.
4.  **Architected** a Kubernetes cluster with Ingress.
5.  **Hardened** your workspace with DevContainers.

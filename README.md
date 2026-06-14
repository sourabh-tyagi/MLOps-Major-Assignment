# MLOps Major Assignment

## Overview

This project demonstrates an end-to-end Machine Learning Operations (MLOps) workflow using:

* Scikit-Learn
* Decision Tree Classifier
* Git & GitHub
* GitHub Actions (CI/CD)
* Flask
* Docker
* Docker Hub
* Kubernetes

The machine learning model is trained on the Olivetti Faces Dataset and deployed as a containerized web application capable of predicting face classes from uploaded images.

The application also uses an *uploads/* directory to temporarily store images uploaded by users for prediction. Since uploaded files are generated at runtime and may vary between executions, the *uploads/* folder is excluded from version control through the .gitignore file.

---

# Prerequisites

Before running the project, ensure the following software is installed:

* Python 3.11 or later
* Anaconda or Miniconda
* Git
* Docker Desktop
* Kubernetes (Minikube, Docker Desktop Kubernetes, or any Kubernetes cluster)

---

# Environment Setup

## Clone the Repository

```
git clone https://github.com/sourabh-tyagi/MLOps-Major-Assignment.git
cd MLOps-Major-Assignment
```

## Create Conda Environment

```
conda create -n mlops_major python=3.11
```

## Activate Environment

```
conda activate mlops_major
```

## Install Dependencies

```
pip install -r requirements.txt
```

---

# Branch Structure

The repository follows a three-branch workflow.

## main Branch

Purpose:

* Repository initialization
* Base branch setup

Contains:

* README.md
* .gitignore

---

## dev Branch

Purpose:

* Machine Learning model development
* Model training and testing
* Continuous Integration setup

Contains:

```
.github/workflows/ci.yml
requirements.txt
savedmodel.pth
train.py
test.py
README.md
.gitignore
```

Commands:

```
python train.py
python test.py
```

---

## docker_cicd Branch

Purpose:

* Flask application deployment
* Docker containerization
* Docker Hub integration
* Kubernetes deployment
* Complete CI/CD implementation

Contains:

```
.github/
└── workflows/
    └── ci.yml

k8s/
├── deployment.yaml
└── service.yaml

templates/
└── index.html

uploads/

app.py
Dockerfile
requirements.txt
savedmodel.pth
train.py
test.py
README.md
.gitignore
```

---

# Project Structure

```
MLOps-Major-Assignment/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── app.py
├── train.py
├── test.py
├── requirements.txt
├── Dockerfile
├── savedmodel.pth
├── README.md
└── .gitignore
```

---

# Dataset

Dataset Used:

* Olivetti Faces Dataset

Dataset Information:

* 400 grayscale face images
* 40 unique individuals
* 10 images per individual
* Image size: 64 × 64 pixels

Source:

* Scikit-Learn built-in dataset

---

# Model Training

The training script performs the following tasks:

* Loads the Olivetti Faces Dataset
* Splits the dataset into training and testing sets
* Trains a Decision Tree Classifier
* Saves the trained model for future inference

Run the training script:

```
python train.py
```

Generated Artifact:

```
savedmodel.pth
```

---

# Model Testing

The testing script evaluates the trained model using the test dataset.

Run the testing script:

```
python test.py
```

---

# GitHub Actions CI/CD

GitHub Actions workflow automatically:

* Checks out repository code
* Installs project dependencies
* Executes train.py
* Executes test.py
* Validates successful execution

Workflow Location:

```
.github/workflows/ci.yml
```

---

# Flask Web Application

Run locally:

```
python app.py
```

Application URL:

```
http://localhost:5000
```

Features:

* Image upload
* Face class prediction
* Uploaded image preview
* Dataset information display
* Prediction result display

---

# Docker

## Build Docker Image

```
docker build -t mlops-face-app:v2 .
```

## Verify Image

```
docker images
```

## Run Container

```
docker run -p 5000:5000 mlops-face-app:v2
```

Application URL:

```
http://localhost:5000
```

Benefits:

* Consistent deployment environment
* Easy portability
* Simplified application distribution

---

# Docker Hub

Repository:

https://hub.docker.com/r/sourabhtyagi/mlops-face-app

Push Commands:

```
docker tag mlops-face-app:v2 sourabhtyagi/mlops-face-app:v2
docker push sourabhtyagi/mlops-face-app:v2
```

Purpose:

* Store Docker images remotely
* Enable image versioning
* Simplify Kubernetes deployments

---

# Kubernetes

## Deployment

Apply deployment:

```
kubectl apply -f k8s/deployment.yaml
```

Verify deployment:

```
kubectl get deployments
kubectl get pods
```

Deployment Configuration:

* 3 replicas
* Container image from Docker Hub
* Automatic pod recovery
* High availability through replication

---

## Service

Apply service:

```
kubectl apply -f k8s/service.yaml
```

Verify service:

```
kubectl get svc
```

Service Type:

```
NodePort
```

Port Mapping:

```
5000 → 30007
```

Application Access:

```
http://localhost:30007
```

---

# Kubernetes Self-Healing Demonstration

Delete a running pod:

```
kubectl delete pod <pod-name>
```

Monitor pod status:

```
kubectl get pods -w
```

Expected Behavior:

* Kubernetes detects the missing pod
* A new pod is automatically created
* Desired replica count is maintained
* Application availability remains unaffected

This demonstrates Kubernetes self-healing and fault-tolerance capabilities.

---

# Technologies Used

* Python 3.11
* Scikit-Learn
* NumPy
* Flask
* Git
* GitHub
* GitHub Actions
* Docker
* Docker Hub
* Kubernetes

---

# Author

**Sourabh Tyagi**

MLOps Major Assignment
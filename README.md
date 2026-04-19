# 🚀 Containerized DevOps Project — CI/CD Pipeline on Azure

## Project Overview
A production-style CI/CD pipeline that automatically builds and deploys 
a Flask web application using Jenkins, Docker, and GitHub on Azure.

## Tech Stack
| Tool | Purpose |
|------|---------|
| Azure VM (Ubuntu) | Cloud infrastructure |
| Docker | Containerization |
| Jenkins | CI/CD automation |
| GitHub | Source code management |
| Python Flask | Web application |

## Architecture# Cloud_DevOps-Projects

## Pipeline Stages
1. **Clone** — Jenkins pulls latest code from GitHub
2. **Build** — Docker builds image from Dockerfile
3. **Deploy** — Old container replaced with new one automatically

## How to Run Locally
```bash
git clone https://github.com/Pragathiramji96/Cloud_DevOps-Projects.git
cd Cloud_DevOps-Projects
docker build -t cloudnote-app .
docker run -d -p 5000:5000 cloudnote-app
```

## Live Demo
- App: `http://20.244.27.88:5000`
- Jenkins: `http://20.244.27.88:8080`

## Screenshots

### ✅ Application Running on Azure
![App](App.png)

### ✅ Jenkins Pipeline Success
![Jenkins](Jenkins_Successful.png)

### ✅ Azure VM Dashboard
![Azure](Azure-vm.png)
### Live App
![App Running](docs/app-screenshot.png)

### Jenkins Pipeline Success
![Jenkins Success](docs/jenkins-screenshot.png)

## What I Learned
- Setting up Linux server on Azure cloud
- Installing and configuring Jenkins via Docker
- Writing Dockerfiles and building container images
- Creating Jenkins pipeline using Jenkinsfile (Groovy)
- Full CI/CD flow from code push to auto deployment

## Author
**Pragathi** — DevOps Engineer in Training

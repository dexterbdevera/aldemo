# API Viewer Web App
> Powered by Python Django Web Framework
----
## Overview

This project aims to develop an API web application client and implement a CI/CD (Continuous Integration/Continuous Deployment) pipeline to facilitate seamless deployment to a cloud-based Kubernetes environment. 

The client will consume various APIs and provide a user-friendly interface to interact with the backend services. 

The CI/CD pipeline will automate the build, testing, and deployment processes, ensuring rapid and efficient software delivery.

**Goals**:
- Develop a robust and scalable API web application client that integrates with backend services.
- Implement a CI/CD pipeline to automate the build, test, and deployment stages.
- Deploy the client application to a cloud-based Kubernetes cluster for high availability and scalability.
- Enable seamless updates and rollbacks of the application using the CI/CD pipeline.

**Key Features**:
- **API Integration**: The client application will consume multiple APIs to retrieve and display relevant data.
- **User-Friendly Interface**: The client will provide an intuitive interface for users to interact with the backend services.
- **Automated Testing**: Implement unit tests, integration tests, and end-to-end tests to ensure the application's quality.
- **Version Control**: Utilize a version control system (e.g., Git) to manage source code and enable collaboration.
- **CI/CD Pipeline**: Set up an automated pipeline to build, test, and deploy the application to the Kubernetes cluster.
- **Scalable Deployment**: Deploy the application to a cloud-based Kubernetes environment to leverage scalability and high availability.

**Technology Stack**:
- **Frontend**: HTML, CSS, Python and Django web framework
- **Backend APIs**: RESTful APIs 
- **Version Control**: Git / GitHub
- **CI/CD Pipeline**: Jenkins
- **Containerization**: Docker to package the application and its dependencies
- **Orchestration**: Kubernetes to manage containerized deployments
- **Cloud Platform**: Microsoft Azure - Azure Kubernetes Cluster

*Project Phases**:
- **Requirement Gathering**: Understand the client's requirements and define the scope of the project.
- **Design and Development**: Design the application architecture, develop frontend and backend components, and integrate the APIs.
- **Testing**: Create and execute various tests to ensure the application functions correctly and meets the requirements.
- **CI/CD Pipeline Setup**: Configure the CI/CD pipeline, including build triggers, testing automation, and deployment stages.
- **Kubernetes Deployment**: Set up a cloud-based Kubernetes cluster and deploy the application using containerization techniques.
- **Monitoring and Maintenance**: Implement monitoring tools and processes to track the application's performance and apply necessary updates or fixes.

**Deliverables**:
- API web application client with a user-friendly interface.
- Fully functional CI/CD pipeline for automated build, test, and deployment processes.
- Deployed application running on a cloud-based Kubernetes cluster.
- Documentation covering architecture, setup instructions, and maintenance guidelines.

## Web Application

The API Viewer web application is developed using `Python` and `Django` web framework.

The webapp will serve as a REST client that will send HTTP requests or API calls, and receive the response in either XML or JSON format.

![image](https://github.com/dexterbdevera/aldemo/assets/90995830/05885352-a323-4b1b-a0a3-c2e434884cd3)

The `python` scripts that will perform the API calls are:
- SIDs [sids.py](https://github.com/dexterbdevera/aldemo/blob/main/code/src/sids.py)
- STARs [stars.py](https://github.com/dexterbdevera/aldemo/blob/main/code/src/stars.py)

The data structure used is `python` dictionary & list for faster processing of data.

## Continuous Integration & Continuous Delivery

`Jenkins` will be the CI/CD tool that has the following stages:

- **Code Checkout** - clone the code from `Github`.
- **OWASP Dependency Check** - code scan to detect publicly disclosed vulnerabilities contained within a project’s dependencies.
- **Docker Build** - containerize the webapp with `Docker` container.
- **Docker Push** - published the Docker image into `DockerHub` container registry.
- **App Deploy to AKS** -  deploy the dockerized webapp as pods into `Azure Kubernetes Service (AKS) cluster`.

Below is the complete DevSecOps CI/CD pipeline architecture diagram and workflow that will deploy our API Viewer web app into AKS:

![image](https://github.com/dexterbdevera/aldemo/assets/90995830/1742feeb-c4da-4883-a463-ef46cd30c662)

The `Azure Kubernetes Service (AKS)` cluster is provisioned using `Terraform`:
- [main.tf](https://github.com/dexterbdevera/aldemo/blob/main/terraform/main.tf)
- [variables.tf](https://github.com/dexterbdevera/aldemo/blob/main/terraform/variables.tf)
- [secret.tfvars](https://github.com/dexterbdevera/aldemo/blob/main/terraform/secret.tfvars)

## 💫 About Me:
just a passionate DevSecOps, Automation and Cloud guy =)

## 🌐 Socials:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/dexterbdevera) 

## 💻 Tech Stack:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E) ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white) ![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white) ![Azure](https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=azure-devops&logoColor=white) ![Google Cloud](https://img.shields.io/badge/Google%20Cloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white) ![IOS](https://img.shields.io/badge/IOS-%2320232a.svg?style=for-the-badge&logo=apple&logoColor=white) ![ANDROID](https://img.shields.io/badge/android-%2320232a.svg?style=for-the-badge&logo=android&logoColor=%a4c639) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Apache](https://img.shields.io/badge/apache-%23D42029.svg?style=for-the-badge&logo=apache&logoColor=white) ![Jenkins](https://img.shields.io/badge/jenkins-%232C5263.svg?style=for-the-badge&logo=jenkins&logoColor=white) ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![LINUX](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white) ![Confluence](https://img.shields.io/badge/confluence-%23172BF4.svg?style=for-the-badge&logo=confluence&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![ElasticSearch](https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch) ![Jira](https://img.shields.io/badge/jira-%230A0FFF.svg?style=for-the-badge&logo=jira&logoColor=white) ![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white) ![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)

## 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=dexterbdevera&theme=dark&hide_border=true&include_all_commits=false&count_private=false)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=dexterbdevera&theme=dark&hide_border=true)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=dexterbdevera&theme=dark&hide_border=true&include_all_commits=false&count_private=false&layout=compact)
---
[![](https://visitcount.itsvg.in/api?id=dexterbdevera&icon=0&color=0)](https://visitcount.itsvg.in)

## 💰 You can help me by Donating
[![PayPal](https://img.shields.io/badge/PayPal-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/dexdvguitars) 

<!-- Proudly created with GPRM ( https://gprm.itsvg.in ) -->



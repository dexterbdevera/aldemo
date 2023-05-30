# API Viewer Web App
> Powered by Python Django Web Framework
----
## Overview

The API Viewer web application is developed using Python and Django web framework.

Jenkins will be the CI/CD tool that has the following stages:

- Code Checkout - clone the code from Github.
- OWASP Dependency Check - code scan to detect publicly disclosed vulnerabilities contained within a project’s dependencies.
- Docker Build - containerize the webapp with Docker container
- Docker Push - published the Docker image into DockerHub container registry
- App Deploy to AKS -  deploy the dockerized webapp as pods into Azure Kubernetes Service (AKS) cluster

The `python` scripts that will perform the API calls are:
- SIDs [sids.py](https://github.com/dexterbdevera/aldemo/blob/main/code/src/sids.py)
- STARs [stars.py](https://github.com/dexterbdevera/aldemo/blob/main/code/src/stars.py)

Below is the complete CI/CD pipeline architecture diagram and workflow that will deploy our API Viewer web app into AKS:

![image](https://github.com/dexterbdevera/aldemo/assets/90995830/1742feeb-c4da-4883-a463-ef46cd30c662)

The Azure Kubernetes Service (AKS) cluster is provisioned using Terraform:
- [main.tf](https://github.com/dexterbdevera/aldemo/blob/main/terraform/main.tf)
- [variables.tf](https://github.com/dexterbdevera/aldemo/blob/main/terraform/variables.tf)
- [secret.tfvars](https://github.com/dexterbdevera/aldemo/blob/main/terraform/secret.tfvars)

## 💫 About Me:
just a passionate DevOps, Automation and Cloud guy =)

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



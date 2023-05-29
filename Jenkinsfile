pipeline {

    agent any

    environment {
        dockerImage = ''
        registry = 'dexdv/app'
        registryCredential = 'dockerhub_id'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/dexterbdevera/aldemo']])
                
            }
        }
        stage('Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '--format HTML', odcInstallation: 'OWASP-DPC'
                
            }
        }
        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        stage('Publish Image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy App to AKS') {
            steps{
                script {
                    kubernetesDeploy(
                        configs: 'k8s-deployment.yaml',
                        kubeconfigId: 'K8',
                        enableConfigSubstitution: true
                        )
                }
            }
        }
    }
}pipeline {

    agent any

    environment {
        dockerImage = ''
        registry = 'dexdv/app'
        registryCredential = 'dockerhub_id'
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/dexterbdevera/aldemo']])
                
            }
        }
        stage('Dependency Check') {
            steps {
                dependencyCheck additionalArguments: '--format HTML', odcInstallation: 'OWASP-DPC'
                
            }
        }
        stage('Build Image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }
            }
        }
        stage('Publish Image') {
            steps {
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }

        stage('Deploy App to AKS') {
            steps{
                script {
                    kubernetesDeploy(
                        configs: 'k8s-deployment.yaml',
                        kubeconfigId: 'K8',
                        enableConfigSubstitution: true
                        )
                }
            }
        }
    }
}
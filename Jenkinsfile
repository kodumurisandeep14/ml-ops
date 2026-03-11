pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/kodumurisandeep14/ml-ops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-fastapi-app .'
            }
        }
        stage('Stop Old Container') {
            steps {
                'docker stop ml-container || true
                docker rm ml-container || true'
            }
        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 fastapi-ml'
            }
        }

    }
}
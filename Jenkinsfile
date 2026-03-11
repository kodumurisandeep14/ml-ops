pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ml-fastapi-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop ml-container || true
                docker rm ml-container || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name ml-container ml-fastapi-app'
            }
        }

    }
}

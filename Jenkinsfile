pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pragathiramji96/Cloud_DevOps-Projects.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t cloudnote-app:latest .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                    docker stop cloudnote || true
                    docker rm cloudnote || true
                    docker run -d \
                        --name cloudnote \
                        -p 5000:5000 \
                        cloudnote-app:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}

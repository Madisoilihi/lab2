pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("jaayshaun/lab2:latest")
                }
            }
        }
        stage('Push') {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com', 'docker-credentials-id') {
                        docker.image("jaayshaun/lab2:latest").push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }
}


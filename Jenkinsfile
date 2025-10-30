pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }

        stage('Build React Docker Image') {
            steps {
                dir('frontend') {
                    sh 'docker build -t react-flask-app-frontend .'
                }
            }
        }

        stage('Build Flask Docker Image') {
            steps {
                dir('backend') {
                    sh 'docker build -t react-flask-app-backend .'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                sh 'kubectl apply -f k8s/flask-deployment.yaml'
                sh 'kubectl apply -f k8s/react-deployment.yaml'
            }
        }
    }
}

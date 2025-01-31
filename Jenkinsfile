pipeline {
    agent any

    environment {
        // Define environment variables if needed
        DOCKER_IMAGE = 'my-app-image'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the Git repository
                git 'https://github.com/Mupparaju19/shopping-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install npm dependencies
                sh 'npm install'
            }
        }

        stage('Build') {
            steps {
                // Build your app (you can replace this with your specific build commands)
                sh 'npm run build'
            }
        }

        stage('Test') {
            steps {
                // Run tests (optional stage)
                sh 'npm test'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Deploy the application to Kubernetes
                // Apply the deployment and service YAML files
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        always {
            // Clean up or notify after the pipeline is done
            echo 'Pipeline completed.'
        }
    }
}

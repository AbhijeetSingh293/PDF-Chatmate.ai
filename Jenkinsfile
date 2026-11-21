
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Downloading PDF Chatmate source code...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                bat 'python --version'
                bat 'python -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Running PDF Chatmate tests...'
                bat 'venv\\Scripts\\python.exe -m pytest -v --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit testResults: 'test-results.xml',
                  allowEmptyResults: true
        }

        success {
            echo 'PDF Chatmate CI Pipeline completed successfully!'
        }

        failure {
            echo 'PDF Chatmate CI Pipeline failed. Check the console output.'
        }
    }
}

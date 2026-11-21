
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

        stage('OWASP Dependency Scan') {
            steps {
                echo 'Scanning project dependencies for vulnerabilities...'

                dependencyCheck(
                    odcInstallation: 'DP-Check',
                    additionalArguments: '--scan . --format HTML --format XML --out dependency-check-report'
                )
            }
        }
    }

    post {
        always {
            junit testResults: 'test-results.xml',
                  allowEmptyResults: true

            dependencyCheckPublisher(
                pattern: 'dependency-check-report/dependency-check-report.xml',
                skipNoReportFiles: true
            )
        }

        success {
            echo 'PDF Chatmate CI Pipeline completed successfully!'
        }

        failure {
            echo 'PDF Chatmate CI Pipeline failed. Check the console output.'
        }
    }
}

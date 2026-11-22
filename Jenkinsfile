
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        // Stage 1: Checkout source code from GitHub
        stage('Checkout') {
            steps {
                echo 'Downloading PDF Chatmate source code...'
                checkout scm
            }
        }

        // Stage 2: Check Python installation and create virtual environment
        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment...'
                bat 'python --version'
                bat 'python -m venv venv'
            }
        }

        // Stage 3: Install project dependencies
        stage('Install Dependencies') {
            steps {
                echo 'Installing project dependencies...'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        // Stage 4: Run automated tests
        stage('Run Automated Tests') {
            steps {
                echo 'Running PDF Chatmate tests...'
                bat 'venv\\Scripts\\python.exe -m pytest -v --junitxml=test-results.xml'
            }
        }

        // Stage 5: OWASP Dependency-Check security scan
        stage('OWASP Dependency Scan') {
            steps {
                echo 'Scanning project dependencies for vulnerabilities...'

                bat 'if not exist dependency-check-report mkdir dependency-check-report'

                dependencyCheck(
                    odcInstallation: 'DP-Check',
                    nvdCredentialsId: 'nvd-api-key',
                    additionalArguments: '--scan requirements.txt --format HTML --format XML --out dependency-check-report'
                )
            }
        }

        
        // Stage 6: Verify Docker connectivity
        stage('Check Docker Access') {
            steps {
                echo 'Checking Docker access from Jenkins...'
                bat 'docker --version'
                bat 'docker compose version'
                bat 'docker info'
            }
        }

    }

    // Publish test and security reports
    post {
        always {
            junit(
                testResults: 'test-results.xml',
                allowEmptyResults: true
            )

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

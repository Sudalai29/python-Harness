pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root:root' // Run container as root to avoid permission issues
        }
    }

    environment {
        JOB_NAME = "${env.JOB_NAME}"
        BUILD_NUMBER = "${env.BUILD_NUMBER}"
    }

    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                    echo "Updating apt and installing system dependencies..."
                    apt-get update && apt-get install -y \
                        build-essential \
                        libyaml-dev \
                        python3-dev \
                        gcc \
                        && rm -rf /var/lib/apt/lists/*

                    echo "Upgrading pip..."
                    pip install --upgrade pip
                    python --version
                    pip --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing Python dependencies..."
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    pytest tests/
                '''
            }
        }

        stage('Security Scan with Bandit') {
            steps {
                sh '''
                    echo "Running Bandit security scan..."
                    bandit -r src/
                '''
            }
        }

        stage('Dependency Vulnerability Check') {
            steps {
                sh '''
                    echo "Checking dependencies for vulnerabilities..."
                    safety check
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                sh '''
                    echo "Running linting and code quality checks..."
                    flake8 src/
                    pylint src/
                '''
            }
        }

        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: '**/reports/**', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            withCredentials([string(credentialsId: 'python', variable: 'JENKINS_API_TOKEN')]) {
                sh '''
                    curl -u "admin:${JENKINS_API_TOKEN}" \
                         -X POST -H "Content-Type: application/json" \
                         -d '{"job_name": "${JOB_NAME}", "build_number": "${BUILD_NUMBER}"}' \
                         https://3a8decf6512f.ngrok-free.app/jenkins-webhook
                '''
            }
            echo 'Pipeline completed!'
        }
    }
}

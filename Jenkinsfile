pipeline {
    agent any   // use any available agent (switch to docker if plugin installed)

    options {
        timestamps()
    }

    // comment out instead of empty block
    // environment {
    //     SONAR_HOST_URL = 'http://13.203.26.146:9000/'
    //     SONAR_TOKEN = 'sqa_8f74799cbc077791d357a7583caf7671c206ed36'
    // }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    echo "Setting up Python environment"
                    python3 --version
                    pip3 install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    echo "Installing dependencies"
                    pip3 install -r requirements.txt
                    pip3 install pytest pytest-cov bandit safety
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                    echo "Running unit tests"
                    python3 -m pytest test_calculator.py -v --cov=calculator --cov-report=xml --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit '**/test-results.xml'
                }
            }
        }

        stage('Security Scan with Bandit') {
            steps {
                sh '''
                    echo "Running security analysis with Bandit"
                    bandit -r . -f json -o bandit-report.json || true
                    bandit -r . || true
                '''
            }
        }

        stage('Dependency Vulnerability Check') {
            steps {
                sh '''
                    echo "Checking for vulnerable dependencies"
                    safety check --json --output safety-report.json || true
                    safety check || true
                '''
            }
        }

        stage('Code Quality Check') {
            steps {
                sh '''
                    echo "Running code quality checks"
                    pip3 install flake8 pylint
                    flake8 calculator.py --max-line-length=120 --output-file=flake8-report.txt || true
                    pylint calculator.py --output-format=json > pylint-report.json || true
                '''
            }
        }

        // stage('SonarQube Analysis') {
        //     steps {
        //         withSonarQubeEnv('MySonarQube') {
        //             sh '''
        //                 echo "Running SonarQube analysis"
        //                 sonar-scanner -Dsonar.projectKey=calculator \
        //                               -Dsonar.sources=. \
        //                               -Dsonar.host.url=${SONAR_HOST_URL} \
        //                               -Dsonar.login=${SONAR_TOKEN}
        //             '''
        //         }
        //     }
        // }

        stage('Archive Artifacts') {
            steps {
                sh '''
                    echo "Archiving test results and reports"
                    mkdir -p artifacts
                    cp *.xml artifacts/ 2>/dev/null || true
                    cp *.json artifacts/ 2>/dev/null || true
                    cp *.txt artifacts/ 2>/dev/null || true
                    ls -la artifacts/
                '''
                archiveArtifacts artifacts: 'artifacts/**/*', fingerprint: true
            }
        }
    }

    post {
        always {
            // send webhook
            sh """
                curl -X POST -H 'Content-Type: application/json' \
                -d '{"job_name": "${env.JOB_NAME}", "build_number": "${env.BUILD_NUMBER}"}' \
                https://3a8decf6512f.ngrok-free.app/jenkins-webhook
            """
            echo 'Pipeline completed!'
        }
    }
}

pipeline {
    agent any

    environment {
        // Defines a local virtual environment directory
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your SCM (GitHub/GitLab)
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                echo 'Creating virtual environment and installing dependencies...'
                script {
                    // Create venv and install packages listed in requirements.txt
                    sh """
                        python3 -m venv ${VENV_DIR}
                        ./${VENV_DIR}/bin/pip install --upgrade pip
                        ./${VENV_DIR}/bin/pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Lint & Code Quality') {
            steps {
                echo 'Running Flake8 syntax and style checks...'
                script {
                    // Ensures your code meets PEP 8 standards (fails build if major syntax errors exist)
                    // Note: Ensure 'flake8' is listed in your requirements.txt
                    sh "./${VENV_DIR}/bin/flake8 . "
                    // --count --select=E9,F63,F7,F82 --show-source --statistics
                }
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                script {
                    // Runs tests using pytest and generates a JUnit XML report
                    // Note: Ensure 'pytest' is listed in your requirements.txt
                    sh "./${VENV_DIR}/bin/pytest --junitxml=results.xml"
                }
            }
            post {
                always {
                    // Displays interactive test results natively inside the Jenkins UI
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}

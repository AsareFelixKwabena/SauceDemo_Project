pipeline {
    agent any

    environment {
        // Optional: specify Python version or virtual environment if needed
        PYTHON = 'python'
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub
                git branch: 'main', url: 'https://github.com/AsareFelixKwabena/SauceDemo_Project.git'
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Selenium tests with Pytest...'
                sh '''
                    source venv/bin/activate
                    pytest --maxfail=1 --disable-warnings --junitxml=reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit 'reports/results.xml'
        }
        success {
            echo '✅ Build succeeded! All tests passed.'
        }
        failure {
            echo '❌ Build failed! Check test results for details.'
        }
    }
}

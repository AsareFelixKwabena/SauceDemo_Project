pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/AsareFelixKwabena/SauceDemo_Project.git'
            }
        }

        stage('Set up Python') {
            steps {
                echo 'Setting up Python environment on Windows...'
                bat '''
                    "C:\\Users\\QWABENA EL\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Selenium tests with Pytest...'
                bat '''
                    call venv\\Scripts\\activate
                    pytest --maxfail=1 --disable-warnings --junitxml=reports\\results.xml
                '''
            }
        }
    }

    post {
        always {
            echo 'Publishing test results...'
            junit 'reports\\results.xml'
        }
        success {
            echo '✅ Build succeeded! All tests passed.'
        }
        failure {
            echo '❌ Build failed! Check test results for details.'
        }
    }
}

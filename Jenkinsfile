pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Validate Pipeline') {
            steps {
                sh '''
                    . venv/bin/activate
                    python -m py_compile src/*.py
                    echo "✅ Python pipeline validation successful"
                '''
            }
        }

    }

    post {
        success {
            echo '🎉 News Headline Aggregator CI pipeline completed successfully!'
        }

        failure {
            echo '❌ CI pipeline failed. Check the Jenkins console output.'
        }
    }
}

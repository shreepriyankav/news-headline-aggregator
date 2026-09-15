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

                    PYTHONPATH=. pytest -v
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

        stage('Trigger Prefect Pipeline') {
            steps {
                sshagent(['news-ec2-ssh']) {
                    sh '''
                        echo "🚀 Triggering Prefect deployment..."

                        ssh -o StrictHostKeyChecking=no \
                            ubuntu@172.31.35.19 \
                            "cd ~/news-headline-aggregator && \
                             source venv/bin/activate && \
                             prefect deployment run 'news-headline-aggregator/daily-news-aggregator'"
                    '''
                }
            }
        }
    }

    post {

        success {
            echo '🎉 CI pipeline completed successfully!'
            echo '🚀 Prefect news aggregation pipeline triggered successfully!'
        }

        failure {
            echo '❌ Pipeline failed. Check the Jenkins console output.'
        }

        always {
            echo '🏁 Jenkins pipeline execution completed.'
        }
    }
}

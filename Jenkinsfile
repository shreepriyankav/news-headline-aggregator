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
                        echo "⏳ Jenkins will wait for the Prefect flow to complete."

                        ssh -o StrictHostKeyChecking=no \
                            ubuntu@172.31.35.19 \
                            "cd ~/news-headline-aggregator && \
                             source venv/bin/activate && \
                             prefect deployment run 'news-headline-aggregator/daily-news-aggregator' --watch"

                        echo "✅ Prefect flow completed successfully."
                    '''
                }
            }
        }
    }

    post {

        success {
            echo '🎉 NEWS HEADLINE AGGREGATOR PIPELINE COMPLETED SUCCESSFULLY!'
            echo '✅ Jenkins tests passed.'
            echo '✅ Python validation passed.'
            echo '✅ Prefect flow completed successfully.'
            echo '✅ News data pipeline executed successfully.'
        }

        failure {
            echo '❌ NEWS HEADLINE AGGREGATOR PIPELINE FAILED.'
            echo '⚠️ Check the Jenkins console output for the failed stage.'
        }

        always {
            echo '🏁 Jenkins pipeline execution completed.'
        }
    }
}

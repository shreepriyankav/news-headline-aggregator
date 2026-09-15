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
                    echo "🐍 Checking Python version..."
                    python3 --version

                    echo "📦 Creating virtual environment..."
                    python3 -m venv venv

                    . venv/bin/activate

                    echo "⬆️ Upgrading pip..."
                    pip install --upgrade pip

                    echo "📥 Installing project dependencies..."
                    pip install -r requirements.txt

                    echo "✅ Python environment setup completed."
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "🧪 Running Python tests..."

                    . venv/bin/activate

                    PYTHONPATH=. pytest -v

                    echo "✅ All tests passed."
                '''
            }
        }

        stage('Validate Pipeline') {
            steps {
                sh '''
                    echo "🔍 Validating Python source files..."

                    . venv/bin/activate

                    python -m py_compile src/*.py

                    echo "✅ Python pipeline validation successful."
                '''
            }
        }

        stage('Trigger Prefect Pipeline') {
            steps {
                sshagent(['news-ec2-ssh']) {
                    sh '''
                        echo "🚀 Triggering Prefect deployment..."
                        echo "⏳ Jenkins will wait until the Prefect flow reaches a terminal state."

                        ssh -o StrictHostKeyChecking=no \
                            ubuntu@172.31.35.19 \
                            "cd ~/news-headline-aggregator && \
                             source venv/bin/activate && \
                             prefect deployment run \
                             'news-headline-aggregator/daily-news-aggregator' \
                             --watch"

                        echo "✅ Prefect flow completed successfully."
                    '''
                }
            }
        }
    }

    post {

        success {
            echo '=================================================='
            echo '🎉 NEWS HEADLINE AGGREGATOR PIPELINE SUCCESSFUL!'
            echo '=================================================='
            echo '✅ Jenkins checkout completed.'
            echo '✅ Python environment setup completed.'
            echo '✅ Tests passed.'
            echo '✅ Python validation passed.'
            echo '✅ Prefect flow completed successfully.'
            echo '✅ News data pipeline executed successfully.'
            echo '=================================================='
        }

        failure {
            echo '=================================================='
            echo '❌ NEWS HEADLINE AGGREGATOR PIPELINE FAILED!'
            echo '=================================================='
            echo '⚠️ Check the failed stage in the Jenkins console.'
            echo '=================================================='
        }

        always {
            echo '🏁 Jenkins pipeline execution completed.'
        }
    }
}

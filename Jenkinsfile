pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Installing dependencies with pip...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flask flask-pymongo python-dotenv pymongo certifi pytest
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running smoke tests with pytest (no DB needed)...'
                sh '''
                    . venv/bin/activate
                    pytest test_smoke.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Tests passed. Deploying to staging environment...'
                sh '''
                    . venv/bin/activate
                    echo "Simulating deployment to staging server..."
                    echo "Student Registration app deployed to staging successfully."
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
            mail to: 'your-email@example.com',
                 subject: "SUCCESS: Jenkins Build #${env.BUILD_NUMBER}",
                 body: "Pipeline completed successfully. Job: ${env.JOB_NAME}"
        }
        failure {
            echo 'Pipeline failed!'
            mail to: 'your-email@example.com',
                 subject: "FAILURE: Jenkins Build #${env.BUILD_NUMBER}",
                 body: "Pipeline failed. Check: ${env.BUILD_URL}"
        }
    }
}

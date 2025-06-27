pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/prasad1057/AnimalPedia.git'
            }
        }

        stage('Install Requirements') {
            steps {
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    source venv/bin/activate
                    # run your test command (e.g., pytest)
                    echo "No tests yet"
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    source venv/bin/activate
                    python app.py
                '''
            }
        }
    }
}

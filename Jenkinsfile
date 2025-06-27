pipeline {
    agent any

    stages {
        stage('Clone') {
             steps {
                  git url: 'https://github.com/prasad1057/AnimalPedia.git'
                }
            }


        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest tests/'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
            }
        }
    }
}

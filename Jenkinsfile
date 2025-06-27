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
            . venv/bin/activate
            pip install -r requirements.txt
        '''
    }
}

stage('Test') {
    steps {
        sh '''
            . venv/bin/activate
            echo "Tests will go here"
        '''
    }
}

stage('Run Flask App') {
    steps {
        sh '''
            . venv/bin/activate
            python app.py
        '''
    }
}



pipeline {
    agent {
        label 'docker-agent-python'
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                cd NIDS
                pip install -r requirements.txt
                '''
            }
        }
        // ... additional stages ...
    }
}

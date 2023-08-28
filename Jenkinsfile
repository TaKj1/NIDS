pipeline{
            agent{   
                node{
                    label 'docker-agent-python'
                }
                 triggers {
            pollSCM '* * * * *'
        }
    stages{
        stage('Build'){
             steps {
                echo "Building.."
                sh '''
                cd NIDS
                pip install -r requirements.txt
                '''
            }
        }
    }


               }






}
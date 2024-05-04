pipeline {
    agent any
    stages {
        stage ("Clone"){
            steps{
                git(
                    url: "https://github.com/llYOrchll/sicei-DevOps.git",
                    branch: "main",
                    changelog: true,
                    poll: true
                )
            }
        }
        stage ("Build"){
            steps{
                sh 'sudo apt-get install python3.8 python3-pip'
                sh 'pip install fastapi'
            }
        }
        stage ("Deploy"){
            steps{
                sh 'docker build -t sicei-app .'
            }
        }
    }
}
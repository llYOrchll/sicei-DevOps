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
                sh 'install fastapi'
            }
        }
        stage ("Deploy"){
            steps{
                sh 'docker build -t sicei-app .'
            }
        }
    }
}
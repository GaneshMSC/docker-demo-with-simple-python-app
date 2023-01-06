pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'sudo docker build -t flask-app -f Dockerfile .'
        echo"Hello World"
      }
    }
  }
  
}

pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo"Hello Wolrd"
        sh 'sudo docker build -t flask-app -f Dockerfile .'
      }
    }
  }
  
}

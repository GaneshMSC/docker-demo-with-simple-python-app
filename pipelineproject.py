pipeline {
   agent any
   stages {
      stage(chekout) {
        steps {
         echo "hello ganesh"
        }      
      }
      stages {
        stage(checkout 1) {
          steps {
            echo "hello world"
          }
        }
      }
    }
}

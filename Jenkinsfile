pipeline {
	     agent any
	     stages {
	         stage('Build') {
	              steps {
	                 sh 'echo "Hello World"'
	                 sh '''
	                     echo "Multiline shell steps works too"
	                     ls -lah
	                 '''
	             }
	         }      
	         stage('Upload to AWS') {
	              steps {
	                  withAWS(region:'eu-west-1',credentials:'70b751e7-6980-4d32-b3d8-2b74879a7113') {
	                  sh 'echo "Uploading content with AWS creds"'
	                      s3Upload(file:'lambda_function.zip', bucket:'us-east-22222222')
			      s3Upload(file:'lambda-packaged.yaml', bucket:'us-east-22222222')
	             }
	         }
		 stage('Upload to AWS') {
	              steps {
	                  withAWS(region:'eu-west-1',credentials:'70b751e7-6980-4d32-b3d8-2b74879a7113') {
	                  sh 'echo "Uploading content with AWS creds"'
	                      s3Upload(file:'lambda_function.zip', bucket:'us-east-22222222')
			      s3Upload(file:'lambda-packaged.yaml', bucket:'us-east-22222222')
	                  }
	              }	 
	         }
	     }
	}
}

pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: '70b751e7-6980-4d32-b3d8-2b74879a7113') { 
                 sh 'echo "Uploading content with AWS creds"'
                 sh 'zip -r lambda_function.zip index.js lib'
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'lambda-splunk-poc')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'lambda-splunk-poc')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: '70b751e7-6980-4d32-b3d8-2b74879a7113') {
                  sh 'aws cloudformation create-stack --stack-name test51 --template-url "https://lambda-splunk-poc.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM'
                  }
              }
         }
     }
}

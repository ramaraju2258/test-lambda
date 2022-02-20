pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: 'b88fdb60-2c8b-4275-b761-17a120f01186') { 
                 sh 'echo "Uploading content with AWS creds"'
                      sh 'zip lambda_function.zip index.js mysplunklogger.js'
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'cloudformation-test2258')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'cloudformation-test2258')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: 'b88fdb60-2c8b-4275-b761-17a120f01186') {
                  sh 'aws cloudformation create-stack --stack-name testnew56 --template-url "https://cloudformation-test2258.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM'
                  }
              }
         }
     }
}

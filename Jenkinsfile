pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 sh 'aws cloudformation create-stack --stack-name testnew51 --template-url 'https://us-east-22222222.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml' --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM'
             }
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: '70b751e7-6980-4d32-b3d8-2b74879a7113') {
                  sh 'echo "Uploading content with AWS creds"'
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'us-east-22222222')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'us-east-22222222')
                  }
              }
         }
     }
}

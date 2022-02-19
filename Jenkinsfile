pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: '955b46a5-f950-46ea-8a58-f9241d554ea0') { 
                 sh 'echo "Uploading content with AWS creds"'
                      sh 'zip lambda_function.zip index.js lib/mysplunklogger.js'
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'cloudformation-test2258')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'cloudformation-test2258')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: '955b46a5-f950-46ea-8a58-f9241d554ea0') {
                  sh 'aws cloudformation deploy --stack-name testnew33 --template-file "https://cloudformation-test2258.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --parameter-overrides ParamS3Bucket=cloudformation-test2258 ParamS3Key=lambda_function.zip --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM'
                  }
              }
         }
     }
}

pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: 'b88fdb60-2c8b-4275-b761-17a120f01186') { 
                 sh 'echo "Uploading content with AWS creds"'
                      
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'cloudformation-test2258')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'cloudformation-test2258')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: 'b88fdb60-2c8b-4275-b761-17a120f01186') {
                  sh 'aws s3api list-object-versions --bucket cloudformation-test2258 --prefix lambda_function.zip --query 'Versions[?IsLatest].[VersionId]' --output text'
                  sh 'aws cloudformation update-stack --stack-name testnew58 --template-url "https://cloudformation-test2258.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --parameters ParameterKey=ParamS3Bucket,UsePreviousValue=true ParameterKey=ParamS3Key,UsePreviousValue=true ParameterKey=LambdaVersion,ParameterValue=${latest_version}'
                  }
              }
         }
     }
}

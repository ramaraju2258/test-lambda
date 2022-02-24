pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: '372cdc38-3d47-4319-b9cc-b8d1d8a3d902') { 
                 sh 'echo "Uploading content with AWS creds"'
                 sh 'zip -r lambda_function.zip index.js lib'     
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_function.zip', bucket:'us-east-22222222')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'us-east-22222222')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: '372cdc38-3d47-4319-b9cc-b8d1d8a3d902') {
                   sh '''
                   latest_version=$(aws s3api list-object-versions --bucket lambda-splunk-poc --prefix lambda_function.zip --query 'Versions[?IsLatest].[VersionId]' --output text)
                   aws cloudformation update-stack --stack-name test51 --template-url "https://us-east-22222222.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --parameters ParameterKey=ParamS3Bucket,UsePreviousValue=true ParameterKey=ParamS3Key,UsePreviousValue=true ParameterKey=LambdaVersion,ParameterValue=${latest_version}
                   '''
                  }
              }
         }
     }
}

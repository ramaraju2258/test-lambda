pipeline {
     agent any
     stages {
         stage('Build') {
             steps {
                 withAWS(region: 'eu-west-1', credentials: '372cdc38-3d47-4319-b9cc-b8d1d8a3d902') { 
                 sh 'echo "Uploading content with AWS creds"'
                 sh 'zip -r lambda_new.zip lambda_function.py'     
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda_new.zip', bucket:'us-east-22222222')
                      s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'lambda-packaged.yaml', bucket:'us-east-22222222')
                 }
             }       
         }      
         stage('Upload to AWS') {
              steps {
                  withAWS(region: 'eu-west-1', credentials: '372cdc38-3d47-4319-b9cc-b8d1d8a3d902') {
                   sh '''
                   latest_version=$(aws s3api list-object-versions --bucket us-east-22222222 --prefix lambda_new.zip --query 'Versions[?IsLatest].[VersionId]' --output text)
                   echo ${latest_version}
                   aws cloudformation deploy --stack-name test795 --template-file lambda-packaged.yaml --parameter-overrides ParamS3Bucket=us-east-22222222 ParamS3Key=lambda_new.zip LambdaVersion=${latest_version}
                   '''
                  }
              }
         }
     }
}

pipeline {
  agent any
  stages {
    stage('Upload to AWS') {
      steps {
        withAWS(region: 'eu-west-1', credentials: '70b751e7-6980-4d32-b3d8-2b74879a7113') {
          sh 'echo "Uploading content with AWS creds"'
          s3Upload(file: 'lambda_function.zip', bucket: 'us-east-22222222')
          s3Upload(file: 'lambda-packaged.yaml', bucket: 'us-east-22222222')
        }
      }
      stage('Upload to AWS') {
        steps {
          withAWS(region: 'eu-west-1', credentials: '70b751e7-6980-4d32-b3d8-2b74879a7113') {
            sh 'echo "Uploading content with AWS creds"'
            aws cloudformation create-stack --stack-name testnew48 --template-url "https://cloudformation-test2258.s3.eu-west-1.amazonaws.com/lambda-packaged.yaml" --region eu-west-1 --capabilities CAPABILITY_NAMED_IAM
          }
        }
      }
    }
  }
}

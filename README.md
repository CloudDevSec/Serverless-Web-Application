# Serverless Web Application

This project develops a serverless web application using AWS Lambda, API Gateway, DynamoDB, and S3.

## Technologies

- AWS Lambda
- AWS API Gateway
- AWS DynamoDB
- AWS S3

## Installation and Usage

### Prerequisites

1. AWS CLI configured with the necessary permissions.
2. AWS SAM CLI for local development and testing.

### Deployment

1. Build and package the application:
    ```bash
    sam build
    sam package --output-template-file packaged.yaml --s3-bucket YOUR_S3_BUCKET_NAME
    ```

2. Deploy the application:
    ```bash
    sam deploy --template-file packaged.yaml --stack-name serverless-webapp --capabilities CAPABILITY_IAM
    ```

## Contact

Sascha Meyer 

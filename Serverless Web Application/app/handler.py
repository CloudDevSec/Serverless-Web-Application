import json

def lambda_handler(event, context):
    body = {
        "message": "Hello, this is the Serverless Web App by Sascha!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

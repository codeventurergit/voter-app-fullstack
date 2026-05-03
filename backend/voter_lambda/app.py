import json
import boto3
import os
from botocore.exceptions import ClientError

# Initialize the DynamoDB client outside the handler for connection re-use

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ.get('TABLE_NAME', 'VoterData')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """
    AWS Lambda function to fetch voter insights from DynamoDB.
    """
    try:
        # Scan the table to get all items
        # Note: For large datasets, I would use Query or Pagination
        response = table.scan()
        items = response.get('Items', [])

        # Return a successful response with CORS headers
        # (CORS is essential so your React app can talk to this API)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*", # Allows React to connect
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(items)
        }

    except ClientError as e:
        print(f"Error accessing DynamoDB: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Could not retrieve voter data"})
        }

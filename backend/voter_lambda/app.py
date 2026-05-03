import json
import boto3
import os
from botocore.exceptions import ClientError

# Initialize the DynamoDB client outside the handler for better performance
dynamodb = boto3.resource('dynamodb')
# Use an environment variable for the table name (best practice for SAM/AWS)
TABLE_NAME = os.environ.get('VOTER_TABLE', 'VoterData')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    """
    Main Lambda entry point. 
    Handles fetching voter data and returning it to your React frontend.
    """
    print(f"Received event: {json.dumps(event)}")
    
    try:
        # 1. Logic: Fetch all items from the VoterData table
        # In a real app, you might add AI manipulation or SQL-like filtering here
        response = table.scan()
        items = response.get('Items', [])

        # 2. Construct the successful response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*", # Required for React to talk to API
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "message": "Success",
                "voter_count": len(items),
                "data": items
            })
        }

    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Could not retrieve voter data"})
        }
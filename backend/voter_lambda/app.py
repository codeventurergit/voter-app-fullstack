import json
import boto3
import os
from decimal import Decimal
from botocore.exceptions import ClientError

# 1. Helper to handle DynamoDB numbers (Decimals)
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert to int if it's a whole number, else float
            if obj % 1 == 0:
                return int(obj)
            return float(obj)
        return super(DecimalEncoder, self).default(obj)

# Initialize resource outside handler for better 'Warm Start' performance
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    """
    Optimized Lambda
    Handles environment variables, Decimal serialization, and CORS.
    """
    print(f"Received event: {json.dumps(event)}")
    
    # Get table name from environment variable injected by SAM
    TABLE_NAME = os.environ.get('TABLE_NAME')
    
    if not TABLE_NAME:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Configuration error: TABLE_NAME not found in environment"})
        }

    table = dynamodb.Table(TABLE_NAME)
    
    try:
        # Fetch data from DynamoDB
        response = table.scan()
        items = response.get('Items', [])

        # Construct response with headers
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "message": "Success",
                "voter_count": len(items),
                "voters": items
            }, cls=DecimalEncoder)
        }

    except Exception as e:
        print(f"Unexpected Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": f"Database error: {str(e)}"})
        }
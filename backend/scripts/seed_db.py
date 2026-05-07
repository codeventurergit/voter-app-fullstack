import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1') # Change region if needed
table = dynamodb.Table('voter-app-stack-VoterData-1CQCUE1WCFLEW') # Use the exact name from your template.yaml

voters = [
    {'voter_id': '1', 'name': 'Jane Doe', 'age': 34, 'party': 'Independent', 'zip_code': '19801'},
    {'voter_id': '2', 'name': 'John Smith', 'age': 52, 'party': 'Democrat', 'zip_code': '19805'},
    {'voter_id': '3', 'name': 'Juan Garcia', 'age': 28, 'party': 'Democrat', 'zip_code': '19703'},
    {'voter_id': '4', 'name': 'Robert Chen', 'age': 64, 'party': 'Independent', 'zip_code': '19802'},
    {'voter_id': '5', 'name': 'Sarah Lancaster', 'age': 41, 'party': 'Republican', 'zip_code': '19901'}
]

print("Starting to seed data...")
with table.batch_writer() as batch:
    for voter in voters:
        batch.put_item(Item=voter)
        print(f"Added: {voter['name']}")

print("Seeding complete! Refresh your browser URL.")
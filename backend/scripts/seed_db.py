import boto3

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('VoterData')

def seed_data():
    voter = {
        'VoterId': 'V-1001',
        'Name': 'Jane Doe',
        'Status': 'Registered',
        'District': '14'
    }
    table.put_item(Item=voter)
    print("Successfully seeded Jane Doe into VoterData!")

if __name__ == "__main__":
    seed_data()
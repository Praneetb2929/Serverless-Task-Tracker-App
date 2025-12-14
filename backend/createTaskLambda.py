import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TasksTable')

def lambda_handler(event, context):
    task_id = str(uuid.uuid4())

    table.put_item(
        Item={
            'task_id': task_id,
            'task_name': event['task_name'],
            'status': 'Pending',
            'created_at': datetime.utcnow().isoformat()
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Task created successfully')
    }

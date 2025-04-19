import json
import os
import boto3

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DYNAMODB_TABLE_NAME')
table = dynamodb.Table(table_name)

def handler(event, context):
    try:
        user_id = event['pathParameters'].get('user_id')

        if not user_id:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing user_id in path'})
            }

        response = table.get_item(Key={'UserID': user_id})
        item = response.get('Item')

        if item:
            return {
                'statusCode': 200,
                'body': json.dumps(item)
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': f'User with ID {user_id} not found'})
            }
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Could not retrieve user data'})
        }

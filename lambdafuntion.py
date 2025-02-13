import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IoT_Sensor_Data')

def lambda_handler(event, context):
    try:
        # Extracting data from IoT payload
        for record in event['Records']:
            payload = json.loads(record['body'])
            device_id = payload.get('device_id')
            temperature = payload.get('temperature')
            humidity = payload.get('humidity', None)  # Optional humidity data
            timestamp = payload.get('timestamp')

            if not device_id or not temperature or not timestamp:
                raise ValueError("Missing required data fields")

            # Store data in DynamoDB
            item = {
                'device_id': device_id,
                'timestamp': timestamp,
                'temperature': temperature
            }
            
            if humidity is not None:
                item['humidity'] = humidity

            table.put_item(Item=item)
            
        return {
            'statusCode': 200,
            'body': json.dumps('Data processed successfully!')
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing data: {str(e)}')
        }

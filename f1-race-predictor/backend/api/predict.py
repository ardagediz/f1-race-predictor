import json
from urllib.request import urlopen

def handler(event, context):
    driver_number = event.get('queryStringParameters', {}).get('driver_number', '55')
    session_key = event.get('queryStringParameters', {}).get('session_key', '9159')
    speed = event.get('queryStringParameters', {}).get('speed', '315')

    url = f'https://api.openf1.org/v1/car_data?driver_number={driver_number}&session_key={session_key}&speed>={speed}'
    response = urlopen(url)
    data = json.loads(response.read().decode('utf-8'))

    return {
        'statusCode': 200,
        'body': json.dumps(data),
        'headers': {
            'Content-Type': 'application/json'
        }
    }

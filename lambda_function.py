def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': '\nhello world',
        'headers': {
            'Content-Type': 'text/plain'
        }
    }

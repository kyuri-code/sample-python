def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': '\nhello world',
        'headers': {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            'Content-Type': 'application/json'
        }
    }

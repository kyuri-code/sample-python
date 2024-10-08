import json
def lambda_handler(event, context):
    # OPTIONSメソッドを通すための設定
    name = 'default'
    if('body' in event) and (event['body'] is not None):
        body = json.loads(event['body'])
        try:
            if(body['name']) and (body['name'] is not None):
                name = body['name']
        except KeyError:
            print('No Name')

    return {
        'statusCode': 200,
        'body': json.dumps('hello world ' + name),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        }
    }

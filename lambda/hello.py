import json


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    jevent = json.dumps(event)
    print(jevent['Records'])
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You sent us a message'
    }
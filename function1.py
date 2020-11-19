import json

def lambda_handler(event, context):
    # TODO implement
    number = int(event['Records'][0]['body'])
    print(f'Lambda function A ---> {number+1}')
    return event

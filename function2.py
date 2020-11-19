import json

def lambda_handler(event, context):
    # TODO implement
    print(event['Records'][0]['body'])
    print("Event for Team B")
    return event

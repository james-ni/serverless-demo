import json
import boto3

sns = boto3.client('sns')


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event['body']
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


def sub_sns(event, context):
    message = event['Records'][0]['Sns']['Message']
    print("From SNS: " + message)
    return message


def pub_sns(event, context):
    message = event['body']
    result = sns.publish(
        TopicArn='arn:aws:sns:ap-southeast-2:642590134761:MyTopic',
        Message=message
    )
    print (result)

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response

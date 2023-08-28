import json
import boto3

mysns =  boto3.client("sns")

def isha(x, y):
    # TODO implement
    mysns.publish(
        Message='criticl alert s3 file deleted',
        Subject='s3 object deleted',
        TopicArn='arn:aws:sns:ap-south-1:413249457651:s3BucketObjectDelete'
          )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

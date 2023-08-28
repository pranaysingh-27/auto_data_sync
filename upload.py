import boto3
import json

def lambda_handler(event, context):
    # Initialize SNS client
    sns_client = boto3.client('sns')
    
    # Publish the message to the SNS topic
    sns_client.publish(
        TopicArn='arn:aws:sns:ap-south-1:413249457651:ChangesINBucket',
        Message="File has been uploaded successfully.",
        Subject='S3 File update'
        )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }

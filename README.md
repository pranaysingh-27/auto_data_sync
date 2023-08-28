# datasync
Automated Data Synchronization System using AWS

Step 1: Set up AWS S3 Buckets Create source and destination Amazon S3 buckets for data transfer.

Step 2: Set up AWS DataSync Task Create an AWS DataSync task to synchronize data between the source and destination buckets. You can create a task through the AWS Management Console or use the AWS CLI

Step 3: Set up AWS Lambda Function for SNS Notifications Create an SNS topic to which you'll subscribe for notifications. Note down the ARN of the topic.Create an AWS Lambda function that sends SNS notifications.

Step 4: Set up CloudWatch Events Rule Create a CloudWatch Events rule that triggers the Lambda function when the DataSync task completes.Add a target to the rule, specifying the ARN of the Lambda function.

Step 5: Subscribe to SNS Topic Subscribe to the SNS topic using an email address or an endpoint, so you receive notifications.

Step 6: Start DataSync Task Start the DataSync task manually or set up a trigger that initiates the task based on your preferred schedule or event.That's it! With these steps, you'll have an automated data synchronization project set up using AWS DataSync and SNS notifications for status updates.

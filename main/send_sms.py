# An example of how to use AWS SNS with Python's boto
# By Alfredo Sanchez @asaguado
# Publish on March 2018
# http://aws.amazon.com/sns/
# https://boto3.readthedocs.io/en/latest/reference/services/sns.html
# https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html


import boto3


# AWS Credentials
AWS_ACCESS_KEY_ID = "AKIAW5FH4YQUNEVYIXP2"
AWS_SECRET_ACCESS_KEY = "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"
AWS_REGION_NAME = "eu-west-1"

SENDER_ID = "Test"
SMS_MESSAGE = "Test"


# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION_NAME
)

# Create the topic if it doesn't exist (this is idempotent)
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

some_list_of_contacts = [
    '+639455703170',
    '+639392014202',
]

# Add SMS Subscribers
for number in some_list_of_contacts:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=number  # <-- number who'll receive an SMS message.
    )

# Publish a message.
response = client.publish(
    Message=SMS_MESSAGE,
    TopicArn=topic_arn,
    MessageAttributes={
        'string': {
            'DataType': 'String',
            'StringValue': 'String',
        },
        'AWS.SNS.SMS.SenderID': {
            'DataType': 'String',
            'StringValue': SENDER_ID
        }
    }
)

print(response)
print("MessageId:" + response["MessageId"])
print("HTTPStatusCode:" + str(response["ResponseMetadata"]["HTTPStatusCode"]))
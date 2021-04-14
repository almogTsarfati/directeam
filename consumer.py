import boto3
import datetime

client = boto3.client('sqs')
s3upload = boto3.resource('s3')


response = client.receive_message(
    QueueUrl='https://sqs.us-east-1.amazonaws.com/430771376827/data_pipeline',
    MessageAttributeNames=[
        'string',
    ]
)

path = 'post_processing/' + str(datetime.datetime.now())
s3upload.Object('queue-msg', path).put(Body=str(response)[])

# print(path)
print(dict(response))
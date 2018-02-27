import boto3
client = boto3.client(
    "sns",
    aws_access_key_id="XXXXXXXXXXX",
    aws_secret_access_key="XXXXXXXXXX",
    region_name='us-east-1'
)

respone = client.publish(
    PhoneNumber="+91XXXXXXXX",
    Message="Hello World!"
)

print(respone)


# # Create the topic if it doesn't exist (this is idempotent)
# topic = client.create_topic(Name="notifications")
# topic_arn = topic['TopicArn']  # get its Amazon Resource Name
#
# some_list_of_contacts=['+91aXXXXXXX','+91XXXXXX']
# # Add SMS Subscribers
# for number in some_list_of_contacts:
#     client.subscribe(
#         TopicArn=topic_arn,
#         Protocol='sms',
#         Endpoint=number  # <-- number who'll receive an SMS message.
#     )
#
# # Publish a message.
# response = client.publish(Message="Good news everyone!", TopicArn=topic_arn)
# print(response)

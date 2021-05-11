import boto3
import access
import csv
phonelist = []
# Read csv file
with open('phone_list.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        phonelist.append(line[0])
del phonelist[0]


# Create an SNS client


client = boto3.client(
    "sns",
    aws_access_key_id= access.access_key,
    aws_secret_access_key= access.secret_access_key,
    region_name= access.region_name)

# Add sms topic
topicname = str(input("input the topic name: "))
topicname = topicname.replace(' ', '')
topic = client.create_topic(Name= topicname)
topic_arn = topic['TopicArn']

# Add SMS Subscribers
for number in phonelist:
    client.subscribe(
        TopicArn=topic_arn,
        Protocol='sms',
        Endpoint=number  
    )

#Publish a message.
client.publish(Message="testing sns", TopicArn=topic_arn)

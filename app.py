import boto3
import linux
import windows
client = boto3.client('ec2')

response = client.run_instances(
    ImageId='ami-071226ecf16aa7d96',
    KeyName='keywindow',
    MinCount=2,
    MaxCount=1,
    InstanceType='t2.micro'
)

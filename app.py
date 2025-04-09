import boto3
import windows
client = boto3.client('ec2')

response = client.run_instances(
    ImageId='ami-071226ecf16aa7d96',
    KeyName='demokey',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro'
)

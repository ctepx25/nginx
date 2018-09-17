#!/usr/bin/env python
import boto3,sys
sqs_arn = sys.argv[1]
function_name = sys.argv[2]
region = sys.argv[3]
access = sys.argv[4]
secret = sys.argv[5]
client = boto3.client('lambda', region_name=region, aws_access_key_id=access, aws_secret_access_key=secret)
response = client.create_event_source_mapping(
    EventSourceArn=sqs_arn,
    FunctionName=function_name,
    Enabled=True
)

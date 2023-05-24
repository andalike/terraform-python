import os
import subprocess
import boto3

import socket

ip_address = socket.gethostbyname(socket.gethostname())

subprocess.call(['pip', 'install', 'boto3'])

os.environ['AWS_ACCESS_KEY_ID'] = ''
os.environ['AWS_SECRET_ACCESS_KEY'] = ''
os.environ['AWS_REGION'] = 'us-east-1'


import boto3
client = boto3.client('lookoutmetrics')
response = client.create_anomaly_detector(
    AnomalyDetectorName='detector1',
    AnomalyDetectorDescription='testing detector',
    AnomalyDetectorConfig={
        'AnomalyDetectorFrequency': 'P1D'
    },
    # KmsKeyArn='string',
    Tags={
        'Name': 'detector'
    }
)
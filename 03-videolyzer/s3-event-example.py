# coding: utf-8
event = {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2019-07-30T23:51:45.547Z', 'eventName': 'ObjectCreated:CompleteMultipartUpload', 'userIdentity': {'principalId': 'AWS:AIDA4KGO6T5GY4QOZ5UUG'}, 'requestParameters': {'sourceIPAddress': '65.203.150.124'}, 'responseElements': {'x-amz-request-id': 'BFEE2332432C8A38', 'x-amz-id-2': 'OR09w+RT8SII6ErGDzEYRdPpGlHQ5DBLQtbH9YxoxSs3eCY+IYFmayhmaYh27gSUnVZqcgWz2pM='}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': '17d04ecf-963c-46e5-9ac9-5b04e1fcb136', 'bucket': {'name': 'niloo-videos-python', 'ownerIdentity': {'principalId': 'A1YEMA6CUL1CCA'}, 'arn': 'arn:aws:s3:::niloo-videos-python'}, 'object': {'key': 'Pexels+Videos+2116123.mp4', 'size': 36611885, 'eTag': '38ec6c9c8039b05ad8509c878a5ffb91-5', 'sequencer': '005D40D80839872471'}}}]}
event
event['Records']
event['Records'][0]['s3']['bucket']
event['Records'][0]['s3']['object']['key']
import urllib
urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])

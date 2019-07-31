# coding: utf-8
event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:846542577485:handleLabelDetectionTopic:bb667455-5fa6-4ce6-93d8-9ab12725336c', 'Sns': {'Type': 'Notification', 'MessageId': '48ac9cba-93c5-57ca-a48e-c9016fec47cc', 'TopicArn': 'arn:aws:sns:us-east-1:846542577485:handleLabelDetectionTopic', 'Subject': None, 'Message': '{"JobId":"a0a2cec2f2c2b562b1210ba3a0430985565996f3ca7afc64bd2ee1ed2a164951","Status":"SUCCEEDED","API":"StartLabelDetection","Timestamp":1564604905754,"Video":{"S3ObjectName":"Pexels Videos 1093664.mp4","S3Bucket":"niloo-videos-python"}}', 'Timestamp': '2019-07-31T20:28:25.953Z', 'SignatureVersion': '1', 'Signature': 'PYzFLl/w6nM70gSzRAqcyRPcnukeVHIftGabPQwW1sB6TdO0f9i2J2yIW793oE1tQxsPyowX/xxapWi0EiEUMYVky9LPwG8d4D2ab05k24qxD88uGiyk290DcOeu9iqpBYHYZI9WeaWXIHwm+fMIdeTjrwRi4CTV96hagDTCcj48zlTrCLKP9dTKob48Qom1t/Z+vLiErw3Q9o9ADx9DajV0QnyDN1h04hzVqzZwlOkaO5zFpBPqXsXLWHBl8cxQxTPqYF2e0zTlItPkU58VoS87hNk411aQ1V8jKBQAVf8cG8+jBI/9qtOGXqxhs66Di+bh39Kf+yCZcxgzBfHzsg==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-6aad65c2f9911b05cd53efda11f913f9.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:846542577485:handleLabelDetectionTopic:bb667455-5fa6-4ce6-93d8-9ab12725336c', 'MessageAttributes': {}}}]}
event
event['Records']
event['Records'][0]['EventSource']
event['Records'][0]['EventVersion']
event['Records'][0]['EventSubscriptionArn']
event['Records'][0]['Sns']
event['Records'][0]['Sns']['Message']
event['Records'][0]['Sns']['Message']['JobId']
import jason
import json
json.loads(event['Records'][0]['Sns']['Message'])
json.loads(event['Records'][0]['Sns']['Message'])['JobId']
get_ipython().run_line_magic('save', 'handle-sns-event-example.py 1-20')

# coding: utf-8
import boto3
session = boto3.Session(profile=pythonAutomation)
session = boto3.Session(profile_name='pythonAutomation')
session
s3 = session.resource('s3')
bucket = s3.create_bucket(Bucket='niloo_recognition_videos')
bucket = s3.create_bucket(Bucket='niloo_recognition_videos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
bucket = s3.create_bucket(Bucket='niloo-recognition-videos', CreateBucketConfiguration={'LocationConstraint': session.region_name})
from pathlib import Path
pathname="C:\Users\nkhatibi\Downloads\Pexels Videos 2116123.mp4"
pathname = "C:\Users\nkhatibi\Downloads\Pexels Videos 2116123.mp4"
pathname = 'C:\Users\nkhatibi\Downloads\Pexels Videos 2116123.mp4'
pathname = 'C:/Users/nkhatibi/Downloads/Pexels Videos 2116123.mp4'
path = Path(pathname).expanduser().resolve()
path
path = Path(pathname).expanduser().resolve().asposix()
bucket.upload_file(str(path), str('Pexels Videos 2116123.mp4'))
rekog_client = session.client('rekognition')
response= rekog_client_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response= rekog_client.start_label_detection(Video={'S3Object': {'Bucket': bucket.name, 'Name': path.name}})
response
job_id = response['JobId']
job_id
result = rekog_client.get_label_detection(JobId=job_id)
result

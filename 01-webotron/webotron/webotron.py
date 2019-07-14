import boto3
import click
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-bucket-objects')
@click.argument('bucket_name')
def list_bucket_objects(bucket_name):
    "List all objects"
    for obj in s3.Bucket(bucket_name).objects.all():
        print(obj)

@cli.command('setup-bucket')
@click.argument('bucket_name')
def setup_bucket(bucket_name):
    "Create s3 bucket and setup as a website"
    s3_bucket = None
    try:
        s3_bucket = s3.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint':session.region_name}
                    )
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedByYou':
            s3_bucket = s3.Bucket(bucket_name)
        else:
            raise e

    #s3_bucket.upload_file('index.html','index.html', ExtraArgs={'ContentType': 'text/html'})
    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[{
          "Sid":"PublicReadGetObject",
          "Effect":"Allow",
          "Principal": "*",
          "Action":["s3:GetObject"],
          "Resource":["arn:aws:s3:::%s/*"
          ]
        }
      ]
    }
    """ % s3_bucket.name
    policy = policy.strip()
    pol = s3_bucket.Policy()
    pol.put(Policy=policy)
    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
            'IndexDocument': {
                'Suffix': 'index.html'
            },
            'ErrorDocument': {
                'Key': 'error.html'
            }
        })
    return
    #url = "http://%s.s3-website.us-east-2.amazonaws.com" % s3_bucket.name

if __name__ == "__main__":
    cli()

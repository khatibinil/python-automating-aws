import boto3
import click
from botocore.exceptions import ClientError
from pathlib import Path
import mimetypes

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

def upload_file(s3_bucket, path, key):
    content_type= mimetypes.guess_type(key)[0] or 'text/plain'
    s3_bucket.upload_file(
            path,
            key,
            ExtraArgs={'ContentType': content_type
            })

@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname,bucket):
    "Sync contents of PATHNAME to BUCKET"
    root=Path(pathname).expanduser().resolve()
    s3_bucket = s3.Bucket(bucket)

    def handle_directory(pathname):
        for p in pathname.iterdir():
            if p.is_dir(): handle_directory(p)
            if p.is_file():
                #p = p.as_posix()
                upload_file(s3_bucket, str(p), str(p.relative_to(root).as_posix()))

    handle_directory(root)


if __name__ == "__main__":
    cli()

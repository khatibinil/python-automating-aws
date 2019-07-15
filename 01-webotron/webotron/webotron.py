
import boto3

import click

from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')


@click.group()
def cli():
    """Webotron deploys websites to AWS"""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets"""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket_name')
def list_bucket_objects(bucket_name):
    """List all objects"""
    for obj in bucket_manager.all_objects(bucket_name):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket_name')
def setup_bucket(bucket_name):
    """Create s3 bucket and setup as a website"""
    bucket = bucket_manager.init_bucket(bucket_name)
    bucket_manager.set_policy(bucket)
    bucket_manager.configure_website(bucket)


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket_name')
def sync(pathname,bucket_name):
    """Sync contents of PATHNAME to BUCKET"""
    bucket_manager.sync_bucket(pathname,bucket_name)


if __name__ == "__main__":
    cli()

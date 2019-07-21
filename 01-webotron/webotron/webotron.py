
import boto3

import click
from bucket import BucketManager
from domain import DomainManager
from certificate import CertificateManager
import util

session = None
bucket_manager = None
domain_manager = None

@click.group()
@click.option('--profile' , default="pythonAutomation", help="Use a given AWS profile.")
def cli(profile):
    """Webotron deploys websites to AWS"""
    global session, bucket_manager,domain_manager
    session_cfg={}
    if profile:
        session_cfg['profile_name'] = profile
    session = boto3.Session(**session_cfg)
    bucket_manager = BucketManager(session)
    domain_manager = DomainManager(session)

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
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket_name)))

@cli.command('list-bucket-objects')
@click.argument('domain_name')
def list_bucket_objects(bucket_name):
    """List all objects"""
    for obj in bucket_manager.all_objects(bucket_name):
        print(obj)

@cli.command('setup-domain')
@click.argument('domain_name')
def setup_domain(domain_name):
    """Setup domain for bucket"""
    bucket = bucket_manager.get_bucket(domain_name) #bucket and domain_name must match for website dns to work
    zone = domain_manager.find_hosted_zone(domain_name) or domain_manager.create_hosted_zone(domain_name)
    endpoint = util.get_endpoint(bucket_manager.get_region_name(bucket))
    a_record = domain_manager.create_s3_domain_record(zone,domain_name,endpoint)
    print("Domain configured: http://{}".format(domain_name))
    print(a_record)

if __name__ == "__main__":
    cli()

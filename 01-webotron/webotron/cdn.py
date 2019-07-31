import uuid

"""Classes for Cloud Front Distributions."""

class CDNManager:

    def __init__(self,session):
        """Manages actions for CloudFront distributions."""
        self.session = session
        self.client = self.session.client('cloudfront')

    def find_matching_distribution(self,domain_name):
        """Find a distribution matching domain_name."""
        paginator = self.client.get_paginator('list_distributions')

        try:
            for page in paginator.paginate():
                for cdn in page['DistributionList']['Items']:
                    for alias in cdn['Aliases']['Items']:
                        if alias == domain_name:
                            return cdn
            return None
        except:
            return None

    def create_cdn(self,domain_name, cert):
        "Create a distribution for domain_name using cert."
        origin_id = 'S3-' + domain_name
        result = self.client.create_distribution(
            DistributionConfig={
                'CallerReference': str(uuid.uuid4()),
                'Aliases': {
                    'Quantity': 1,
                    'Items': [domain_name],
                },
                'DefaultRootObject' : 'index.html',
                'Comment' : 'Created by Webotron',
                'Enabled' : True,
                'Origins' : {
                    'Quantity' : 1,
                    'Items' : [{
                        'Id': origin_id,
                        'DomainName' : '{}.s3.amazonaws.com'.format(domain_name),
                        'S3OriginConfig' : {
                            'OriginAccessIdentity' : ''
                        }
                    }]
                },
                'DefaultCacheBehavior': {
                    'TargetOriginId': origin_id,
                    'ViewerProtocolPolicy': 'redirect-to-https',
                    'TrustedSigners': {
                            'Enabled': False,
                            'Quantity': 0
                    },
                    'ForwardedValues': {
                                    'QueryString': False,
                                    'Cookies': {'Forward': 'all'},
                                    'Headers': { 'Quantity':0},
                                    'QueryStringCacheKeys': {'Quantity': 0}
                    },
                    'DefaultTTL': 86400,
                    'MinTTL': 3600
                },
                'ViewerCertificate': {
                    'ACMCertificateArn': cert['CertificateArn'],
                    'SSLSupportMethod': 'sni-only',
                    'MinimumProtocolVersion': 'TLSv1.1_2016'
                }
            })

        return result['Distribution']

        def await_deploy(self,domain_name):
            """Wait for Cloudfront deploy,emt to complete."""
            waiter = self.client.get_waiter('distribution_deployed')
            waiter.wait(
                Id='Id',
                WaiterConfig={
                    'Delay': 30,
                    'MaxAttempts': 50
                }
            )

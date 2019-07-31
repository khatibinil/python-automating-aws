
from pprint import pprint

"""Classes for ACM certificates."""
class CertificateManager:

    def __init__(self,session):
        """Manages actions for certificates."""
        self.session = session
        self.client = self.session.client('acm', region_name= 'us-west-2')

    def cert_matches(self,cert_arn,domain_name):
        """Compare against all matcing."""
        cert_details= self.client.describe_certificate(CertificateArn=cert_arn)
        #cert_details = self.client.('acm',region_name='us-west-2' )
        alt_names = cert_details['Certificate']['SubjectAlternativeNames']
        for name in alt_names:
            if name == domain_name:
                return True
            if name[0] == "*" and domain_name.endswith( name[1:]):
                return True
        return False

    def find_matching_certificates(self, domain_name):
        """List issued certificates."""
        paginator = self.client.get_paginator('list_certificates')

        for page in paginator.paginate(CertificateStatuses=['ISSUED']):
            for cert in page['CertificateSummaryList']:
                if self.cert_matches(cert['CertificateArn'], domain_name):
                    return cert
        return None

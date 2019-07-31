import boto3

session = boto3.Session(profile_name='pythonAutomation')

ec2 = session.resource('ec2')

 #key_name = 'python_automation_key'

#key_path = key_name + '.pem'

#key = ec2.create_key_pair(KeyName = key_name)

with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)

import os, stat

os.chmod(key_path, stat.S_IRUSR | stat.S_IWUSR)


ec2.images.filter(Owners=['amazon'])
ec2.imagesCollection(ec2.ServiceResource(), ec2.Image)

list(ec2.images.filter(Owners=['amazon']))


session = boto3.Session(profile_name='pythonAutomation')

ec2 = session.resource('ec2')

key = ec2.create_key_pair(KeyName = key_name)

with open(key_path, 'w') as key_file:
    key_file.write(key.key_material)

img = ec2.Image('ami-922914f7')

img.name


ec2_apse2 = session.resource('ec2', region_name='ap-southeast-2')

img_apse2 = ec2_apse2.Image('ami-922914f7')

instances = ec2.create_instances(ImageId=img.id, InstanceType='t2.micro', KeyName=key.key_name, MaxCount=1, MinCount=1)
inst = instances[0]

inst.wait_until_running()

inst.reload()

inst.public_dns_name
'ec2-18-223-20-31.us-east-2.compute.amazonaws.com'


sg_iterator = ec2.security_groups.all()
sg_iterator
print(sg_iterator)
for sg in sg_iterator:
    print(sg)
for sg in sg_iterator:
    sg = sg
sg
sg.security_group.authorize_ingress(IpPermissions=[{
    'FromPort' : 22,
    'ToPort' : 22,
    'IpProtocol': 'TCP',
    'IpRanges': [{'CidrIp': '65.203.150.125/32'}]}
    ])
sg.authorize_ingress(IpPermissions=[{
        'FromPort' : 22,
        'ToPort' : 22,
        'IpProtocol': 'TCP',
        'IpRanges': [{'CidrIp': '65.203.150.125/32'}]}
        ])
ssh -i python_automation_key.pem ec2-user@ec2-18-223-20-31.us-east-2.compute.amazonaws.com
sg.authorize_ingress(IpPermissions=[{
    'FromPort' : 80,
    'ToPort' : 80,
    'IpProtocol': 'TCP',
    'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}
    ])

## Automating aws with Python

## 01-webotron

Webotron is a script that will sync a local directory to an s3 bucket and optionally configure Route53 and CloudFront as well.

###Features
Webotron currently has the following Features
- List buckets
- List objects in a bucket
- Setup and configure s3 bucket as website
- Sync directory with s3 bucket
- Set AWS profile with --profile=<profilename>
- Compare file etags and only upload file if it has changed
- See URL of bucket website

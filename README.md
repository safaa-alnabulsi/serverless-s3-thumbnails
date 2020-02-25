# Serverless S3 Thumbnails Generator

A practical example using Python to deploy a service to generate thumbnails for images that interacts with S3.

## Pre-requisite:

- Nodejs
- Serverless
- Python
- Docker

## Development 

To create the serverless for the first time

    sls create -p sls-s3-thumbnails -t aws-python
To install python plugin for the first time

    sls plugin install -n serverless-python-requirements
    
To create AWS credentials file in ~/.aws

    sls config credentials --provider aws --key <access-key-id> --secret <secret> --profile <profilename>

To invoke function

    sls invoke -f <function-name>
    
To show logs of a function

    sls logs -f <function-name>
    
To tail logs of a function

    sls logs -f <function-name> --tail

## Deployment
To install python packages in [requirements.txt](requirements.txt)

    npm install --save serverless-python-requirements

To package all the files & installed libraries
   
    sls package
   
To deploy all serverless functions and resources to AWS

    sls deploy -v
    
To deploy only the changed function code to AWS

    sls update -v <function-name>
    
To remove all serverless functions and resources deployed to AWS

    sls remove


## References: 

- [Serverless Docs](https://serverless.com/framework/docs/)
- [S3 Boto3 client doc](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
- [Cloudformation S3](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html)
- [Permissions in S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html)
- [Pillow Image module examples](https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#examples)
# serverless-s3-thumbnails

A practical example using Python, deploy a service to generate thumbnails for images that interacts with S3 and use a plugin to properly package your Python dependencies.

## Pre-requisite:

- Nodejs
- Serverless
- Python
- Docker

## Development 

To create the serverless for the first time

    sls create -p sls-s3-thumbnails -t aws-python

To create AWS credentials file in ~/.aws

    sls config credentials --provider aws --key <access-key-id> --secret <secret> --profile <profilename>

To invoke function

    sls invoke -f <function-name>
    
To show logs of a function

    sls logs -f <function-name>
    
To tail logs of a function

    sls logs -f <function-name> --tail

## Deployment

To deploy all serverless functions and resources to AWS

    sls deploy -v
    
To deploy only the changed function code to AWS

    sls update -v <function-name>
    
To remove all serverless functions and resources deployed to AWS

    sls remove

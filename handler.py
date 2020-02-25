import json
import boto3
import logging
from botocore.exceptions import ClientError
from PIL import Image
import glob, os

bucket = 's3-thumbnails'
img_file = 'results.png'
size = 2, 2
prefix = 'thumbnail_'


def hello(event, context):
    print(event)
    s3_client = boto3.client('s3')

    new_img_name = prefix + img_file
    image_to_thumbnail(img_file, new_img_name, size)
    response_body = upload_file('/tmp/'+ new_img_name, bucket, object_name=new_img_name)

    response = {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }

    return response


def upload_file(file_name, bucket, object_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(Filename=file_name, Bucket=bucket, Key=object_name)
    except ClientError as e:
        logging.error(e)
        return False

    return True


def image_to_thumbnail(img_file, new_img_name, size):
    file, ext = os.path.splitext(img_file)
    im = Image.open(img_file)
    im.thumbnail(size)
    im.save('/tmp/'+ new_img_name, "PNG")

def get_uploaded_image():
    pass

def is_not_thumbnail():
    pass

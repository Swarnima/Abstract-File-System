import connexion
import six
import boto3
import boto3.s3
import sys, os
import yaml
from boto.s3.key import Key

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util

with open(os.path.abspath("etc/config.yaml"), 'r') as ymlfile:
    config = yaml.load(ymlfile)
aws_access_key_id = config['cloudmesh']['file-system-config']['amazonS3']['accessKey']
aws_secret_access_key = config['cloudmesh']['file-system-config']['amazonS3']['secretKey']
bucketName = config['cloudmesh']['file-system-config']['amazonS3']['bucket']

session = boto3.Session(aws_access_key_id, aws_secret_access_key)
s3 = session.resource('s3')
client = boto3.client('s3')


def delete_file(fileName):  # noqa: E501
    """List objects by bucket name

    Returns list of objects in bucket # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    s3.Object(bucketName, fileName).delete()
    return 'file deleted'


def download_file(fileName):  # noqa: E501
    """Downloads file from bucket name

    upload file to specified bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    s3.meta.client.download_file(bucketName, fileName, fileName)
    return 'file downloaded'


def list_buckets():  # noqa: E501
    """Get all buckets

    Returns a list of buckets # noqa: E501


    :rtype: List[OUTPUT]
    """
    result = list()
    mybucket = s3.Bucket(bucketName)
    for object in mybucket.objects.all():
        result.append(object.key.encode("utf-8"))      
	
    return result
	
	

def list_objects(bucketName):  # noqa: E501
    """List objects by bucket name

    Returns list of objects in bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str

    :rtype: OUTPUT
    """
    result = list()
    mybucket = s3.Bucket(bucketName)
    for object in mybucket.objects.all():
        result.append(object.key.encode("utf-8"))      
	
    return result



def upload_file(fileName):  # noqa: E501
    """List objects by bucket name

    upload file to specified bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    s3.meta.client.upload_file(fileName, bucketName, fileName)
    return 'uploaded'

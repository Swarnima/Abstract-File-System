import connexion
import six
import boto
import boto.s3
import sys
from boto.s3.key import Key
from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util


def list_objects(bucketName):  # noqa: E501
    """List objects by bucket name
    Returns list of objects in bucket # noqa: E501
    :param bucketName: bucket name
    :type bucketName: str
    :rtype: OUTPUT
    """
    return get_list_objects(bucketName)


def get_list_objects(bucketName):
    conn = boto.connect_s3('AKIAIMQXNJ3UGVP4JSQQ', 'sPoPh2MkaeQ/XIjR8EJFf3FD++QQdaqwqPGkmuv9')
    bucket = conn.get_bucket(bucketName, validate=True)
    print(bucket)
    result = list()
    # To list all buckets in account
    for key in bucket.list():
        result.append(key.name.encode("utf-8"))
    return result
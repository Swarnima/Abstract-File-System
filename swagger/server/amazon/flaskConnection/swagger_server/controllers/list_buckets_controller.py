import connexion
import six
import boto
import boto.s3
import sys
from boto.s3.key import Key

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util


def list_buckets():  # noqa: E501
    """Get all buckets
    Returns a list of buckets # noqa: E501
    :rtype: List[OUTPUT]
    """
    return get_list()


def get_list():
    conn = boto.connect_s3('AKIAIMQXNJ3UGVP4JSQQ', 'sPoPh2MkaeQ/XIjR8EJFf3FD++QQdaqwqPGkmuv9')
    print(conn.get_all_buckets())
    result = list()
    print(result)
    # To list all buckets in account
    for bucket in conn.get_all_buckets():
        result.append(bucket.name.encode("utf-8"))        
    return result

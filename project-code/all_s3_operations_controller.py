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
aws_region = config['cloudmesh']['file-system-config']['amazonS3']['region']
bucketName = config['cloudmesh']['file-system-config']['amazonS3']['bucket']
localPath= config['cloudmesh']['file-system-config']['localPath']

def validate_system():
    if(aws_access_key_id=='' or aws_secret_access_key=='' or bucketName == ''):
	return False
    try:
	session = boto3.Session(aws_access_key_id, aws_secret_access_key)
	print(session)
	s3 = session.resource('s3')
	client = boto3.client('s3')
	return True
    except: 
        print('Amazon S3 is not configured correctly in /etc/config.yaml file')
	return False


def delete_file(fileName):  # noqa: E501
    """List objects by bucket name

    Returns list of objects in bucket # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if(validate_system()):
        try:
	    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
	    s3 = session.resource('s3')
	    client = boto3.client('s3')
	    s3.Object(bucketName, fileName).delete()
            return 'File deleted'
        except:
	    return 'File can not be deleted'
    else:
	return 'Amazon S3 is not configured correctly in /etc/config.yaml file'



def download_file(fileName):  # noqa: E501
    """Downloads file from bucket name

    upload file to specified bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if(validate_system()):
	try:
	    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
    	    s3 = session.resource('s3')
	    client = boto3.client('s3')
	    cwd_dir = os.getcwd()
	    os.chdir(localPath)
	    s3.meta.client.download_file(bucketName, fileName, fileName)
            return 'file downloaded'
	    os.chdir(cwd_dir)
	except:
	    return 'File can not be downloaded'
    else:
	return 'Amazon S3 is not configured correctly in /etc/config.yaml file'


def list_buckets():  # noqa: E501
    """Get all buckets

    Returns a list of buckets # noqa: E501


    :rtype: List[OUTPUT]
    """
    result = list()
    if(validate_system()):
	try:
	    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
	    s3 = session.resource('s3')
   	    client = boto3.client('s3')

            mybucket = s3.Bucket(bucketName)
            for object in mybucket.objects.all():
                result.append(object.key.encode("utf-8"))      
	    return result
        except:
   	    return 'Can not list files'
    else:
	return 'Amazon S3 is not configured correctly in /etc/config.yaml file'



	

def list_objects(bucketName):  # noqa: E501
    """List objects by bucket name

    Returns list of objects in bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str

    :rtype: OUTPUT
    """
    result = list()
    if(validate_system()):
        try:  
  	    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
	    s3 = session.resource('s3')
	    client = boto3.client('s3')
  
	    mybucket = s3.Bucket(bucketName)
            for object in mybucket.objects.all():  
                result.append(object.key.encode("utf-8"))      
	    return result
        except:
  	    return 'Can not list files in bucket'
    else:
	return 'Amazon S3 is not configured correctly in /etc/config.yaml file'



def upload_file(fileName):  # noqa: E501
    """List objects by bucket name

    upload file to specified bucket # noqa: E501

    :param bucketName: bucket name
    :type bucketName: str
    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if(validate_system()):
	try:
	    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
	    s3 = session.resource('s3')
	    client = boto3.client('s3')
	    cwd_dir = os.getcwd()
	    os.chdir(localPath)
	    s3.meta.client.upload_file(fileName, bucketName, fileName)
            return 'File uploaded'
	    os.chdir(cwd_dir)
        except:
	    return 'File can not be uploaded'
    else:
	return 'Amazon S3 is not configured correctly in /etc/config.yaml file'
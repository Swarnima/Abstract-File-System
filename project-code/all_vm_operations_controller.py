import connexion
import six
import os,yaml
from ftplib import FTP

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util

with open(os.path.expanduser("/home/ubuntu/swagger_project/etc/config.yaml"), 'r') as ymlfile:
    config = yaml.load(ymlfile)
hostname = config['cloudmesh']['file-system-config']['VM']['hostName']
username = config['cloudmesh']['file-system-config']['VM']['userName']
password = config['cloudmesh']['file-system-config']['VM']['password']



def delete_vm_file(fileName):  # noqa: E501
    """Delete file

    Deletes file or folder # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    ftp = FTP()
    ftp.connect(hostname ,21)
    ftp.login(username, password)
    print("connected to server")

    try:
        ftp.delete(fileName)
    except:
	return 'Unable to delete file'
    return 'File deleted'


def download_vm_file(fileName):  # noqa: E501
    """Downloads file

    Downloads file # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    ftp = FTP()
    ftp.connect(hostname ,21)
    ftp.login(username, password)
    print("connected to server")


    try:
        ftp.retrbinary("RETR " + fileName,open(fileName, 'wb').write)
    except:
        return "Unable to download file"
    return 'File downloaded'


def list_vm_data():  # noqa: E501
    """Get all buckets

    Returns a list of buckets # noqa: E501


    :rtype: List[OUTPUT]
    """
    ftp = FTP()
    ftp.connect(hostname ,21)
    ftp.login(username, password)
    print("connected to server")


    result = list()
    result.append(ftp.nlst())
    return result


def upload_vm_file(fileName):  # noqa: E501
    """Uploads file

    upload file # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    ftp = FTP()
    ftp.connect(hostname ,21)
    ftp.login(username, password)
    print("connected to server")


    try:
        ftp.storbinary('STOR '+fileName, open(fileName, 'rb')) # this is to store file file
        ftp.sendcmd('SITE CHMOD 777 ' + fileName)
    except:
        return 'Unable to upload file'
    return 'File uploaded'

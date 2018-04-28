import connexion
import six
import os,yaml
from ftplib import FTP

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util

with open(os.path.abspath("etc/config.yaml"), 'r') as ymlfile:
    config = yaml.load(ymlfile)
hostname = config['cloudmesh']['file-system-config']['VM']['hostName']
username = config['cloudmesh']['file-system-config']['VM']['userName']
password = config['cloudmesh']['file-system-config']['VM']['password']
localPath= config['cloudmesh']['file-system-config']['localPath']

def validate_system():
    try:
        ftp = FTP()
        ftp.connect(hostname ,21)
        ftp.login(username, password)
	return True
    except: 
        print('Virtual Machine is not configured correctly in /etc/config.yaml file')
	return False



def delete_vm_file(fileName):  # noqa: E501
    """Delete file

    Deletes file or folder # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if(validate_system()):
        try:
	    ftp = FTP()
            ftp.connect(hostname ,21)
            ftp.login(username, password)
            ftp.delete(fileName)
        except:
            return 'Unable to delete file'
        return 'File deleted'
    else:
	return 'Virtual Machine is not configured correctly in /etc/config.yaml file'



def download_vm_file(fileName):  # noqa: E501
    """Downloads file

    Downloads file # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    if(validate_system()):
        try:
	    ftp = FTP()
            ftp.connect(hostname ,21)
            ftp.login(username, password)
	    cwd_dir = os.getcwd()
	    os.chdir(localPath)	   # local directory as configured in config.yaml
            ftp.retrbinary("RETR " + fileName,open(fileName, 'wb').write)
	    os.chdir(cwd_dir)
        except:
            return "Unable to download file"
        return 'File downloaded'
    else:
	return 'Virtual Machine is not configured correctly in /etc/config.yaml file'


def list_vm_data():  # noqa: E501
    """Get all buckets

    Returns a list of buckets # noqa: E501


    :rtype: List[OUTPUT]
    """
   
    if(validate_system()):
        try:
            ftp = FTP()
            ftp.connect(hostname ,21)
            ftp.login(username, password)
	    result = list()
            result.append(ftp.nlst())
            return result
        except:
     	    return 'Can not retrieve list of files'
    else:
	return 'Virtual Machine is not configured correctly in /etc/config.yaml file'

def upload_vm_file(fileName):  # noqa: E501
    """Uploads file

    upload file # noqa: E501

    :param fileName: file name
    :type fileName: str

    :rtype: None
    """
    
    if(validate_system()):
        try:
   	    ftp = FTP()
            ftp.connect(hostname ,21)
            ftp.login(username, password)
	    cwd_dir = os.getcwd()
	    os.chdir(localPath) # local directory as configured in config.yaml
	    ftp.storbinary('STOR '+fileName, open(fileName, 'rb')) # this is to store file file
            ftp.sendcmd('SITE CHMOD 777 ' + fileName)
	    os.chdir(cwd_dir)
        except:
            return 'Unable to upload file'
        return 'File uploaded'
    else:
	return 'Virtual Machine is not configured correctly in /etc/config.yaml file'


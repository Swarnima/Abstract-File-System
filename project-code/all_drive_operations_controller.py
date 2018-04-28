from __future__ import print_function
import httplib2
import connexion, six, apiclient.discovery, os, io, yaml

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util


# Configured from /etc/config.yaml file 
# To get local path from where files can be uploaded or downloaded to
with open(os.path.abspath("etc/config.yaml"), 'r') as ymlfile:
    config = yaml.load(ymlfile)
localPath= config['cloudmesh']['file-system-config']['localPath']

# Static variables having project level data
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = os.path.abspath('etc/client_id.json')
APPLICATION_NAME = 'file-system'

# check for argument to indicate if the briwser is accessible to autherise the application with google drive for the first time
# optional parameter -- to indicate that user can use any local browser to authenticate

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

def getCredentials():
    try:
	cwd_dir = os.getcwd()
        credential_dir = os.path.abspath('etc')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                   'google-drive-credentials.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:  
               credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        print(credentials)
        return credentials
    except:
	return 'Failed'

def download_drive_file(fileName):  # noqa: E501
    if(getCredentials()=='Failed'):
	return 'Google drive not configured to use Abstract File System'

    else:

        page_token = None
        path = os.getcwd()
        credentials = getCredentials()
        http = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http)
        query = "name='"+str(fileName)+"'"
        print(query)
        response = drive_service.files().list(q=query, spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
	for file in response.get('files', []):
            file_id = file.get('id')
        if(file_id is None):
            return "no file  found"
        else:
            print(file_id)
            request = drive_service.files().get_media(fileId=file_id)
	    name = drive_service.files().get(fileId=file_id).execute()['name']
            handler = io.BytesIO()
            downloader = apiclient.http.MediaIoBaseDownload(handler, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print(int(status.progress() * 100))
	    cwd_dir = os.getcwd()
	    os.chdir(localPath)
            f = open(path + '/' + name, 'wb')
            f.write(handler.getvalue())
            f.close()
	    os.chdir(cwd_dir)
            return ('File downloaded')
 #   except:
#	return 'File can not be downloaded'

def list_data():  # noqa: E501
    if(getCredentials()=='Failed'):
	return 'Google drive not configured to use Abstract File System'


    try:  
	result = list()
        credentials = getCredentials()
        http = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http)
        results = drive_service.files().list(pageSize=20, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            return 'No files found.'
        else:
            print('Files:')
	    result = list()
            for item in items:
	       result.append((item['name']))
            return result
    except:
	return 'Files can not be listed'

def upload_drive_file(fileName):  # noqa: E501
    if(getCredentials()=='Failed'):
	return 'Google drive not configured to use Abstract File System'

    try:
	credentials = getCredentials()
        http = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http)
        mime_type = 'text/plain'
        file_metadata = {'name': fileName}
        cwd_dir = os.getcwd()
	os.chdir(localPath)
        filepath = fileName
        media = apiclient.http.MediaFileUpload(filepath, mime_type)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print('File ID: %s' % file.get('id'))
	os.chdir(cwd_dir)
    except:
	return 'File can not be uploaded'
    return 'File uploaded'

def delete_drive_file(fileName):  # noqa: E501
    if(getCredentials()=='Failed'):
	return 'Google drive not configured to use Abstract File System'

    try:
	page_token = None
        credentials = getCredentials()
        http = credentials.authorize(httplib2.Http())
        drive_service = discovery.build('drive', 'v3', http=http)
        query = "name='"+str(fileName)+"'"
        print(query)
        response = drive_service.files().list(q=query,
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
        for file in response.get('files', []):
            file_id = file.get('id')
        drive_service.files().delete(fileId=file_id).execute()
    except:    
	return 'File can not be deleted'
    return 'File deleted'


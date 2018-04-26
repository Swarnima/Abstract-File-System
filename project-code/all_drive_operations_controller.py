from __future__ import print_function
import httplib2
import connexion, six, apiclient.discovery, os, io

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server import util

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = '/home/ubuntu/swagger_project/etc/client_id.json'
APPLICATION_NAME = 'file-system'
try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

def getCredentials():
    cwd_dir = os.getcwd()
    credential_dir = os.path.join('/home/ubuntu/swagger_project/etc')
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
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def download_drive_file(fileName):  # noqa: E501
    print(fileName)
    page_token = None
    path = os.getcwd()
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
    if(file_id is None):
        return "no file  found"
    else:
        print(file_id)
        request = drive_service.files().get_media(fileId=file_id)
        name = drive_service.files().get(fileId=file_id).execute()['name']
        fh = io.BytesIO()
        downloader = apiclient.http.MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(int(status.progress() * 100))
        f = open(path + '/' + name, 'wb')
        f.write(fh.getvalue())
        print('File downloaded at', path)
        f.close()
        return ('File downloaded')


def list_data():  # noqa: E501
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

def upload_drive_file(fileName):  # noqa: E501
    credentials = getCredentials()
    http = credentials.authorize(httplib2.Http())
    drive_service = discovery.build('drive', 'v3', http=http)
    mime_type = 'text/plain'
    file_metadata = {'name': fileName}
    filepath = fileName
    media = apiclient.http.MediaFileUpload(filepath, mime_type)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print('File ID: %s' % file.get('id'))

    return 'File uploaded'

def delete_drive_file(fileName):  # noqa: E501
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
    return 'File deleted'


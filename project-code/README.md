# RESR Abstract File System SERVICE


The REST Abstract File System Service which is a web services that
implements and abstracts the underlying storage services and provides
a uniform web services APIs for users to do file operations like,
retrieving, storing, removing files on storage services. The service
is provided to support storage engines such as Amazon Simple Storage
Service, google drive and virtual machines. This service can be used
by big data application clients to perform file operations with
consolidated data view.
  

File operations supported by Abstract File System for each storage
engine include:

1. Listing of files 
2. Retrieving specific file
3. Storing file to specified folder
4. Removing file

## Prerequisites for Execution

In order to use different storage systems, it is required to have 
all the systems available and there configurations provided in 
etc/config.yaml file.

To use Amazon S3, it is required to provide access key, secret key,
bucket name is required. 

To use Virtual machine storage it is required to install FTP on that 
machine and create a user with read write access to specified folder.
These specifications such as host name, port, FTP user name and password 
should be provided in config.yaml file

To use google drive storage, it is required to have an Google account. 
When any drive API is used for first time, it will open browser and ask 
user to login to their google drive account and allow access to file-system 
project.


## Test

To test the service follow these steps



### 1. Using Docker

git clone hid-sp18-420.git

cd project-code

Use command ``make container``

This will internally call ``make docker-build`` and ``make docker-start``

Once docker build is successful and container is created, run

    make test

to check the services. Run

    make docker-clean

to remove docker image



### 2. Using make file

git clone hid-sp18-420.git

cd project-code

Use command ``make`` to generate code 

Use command ``make test`` to test the code

Use command ``make clean`` to clean the code


### 2. Using swagger code generator

To use Abstract File System, below python libraries needs to be installed

* pip install boto3
* pip install pyyaml
* pip install --upgrade google-api-python-client


Follow these steps to run Abstract File System project

git clone hid-sp18-420.git

cd project-code

wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

java -jar swagger-codegen-cli-2.3.1.jar generate  -i abstractFileSystem.yaml  -l python-flask  -o server/file-system/flaskConnexion  -D supportPython2=true 

This will generate server stubs. copy all_drive_operations_controller.py, all_s3_operations_controller.py and all_vm_operations_controller.py files to ``/server/file-system/flaskConnexion/swagger_server/controllers``

cd server/file-system/flaskConnexion

pip install -r requirements.txt

python setup.py install

python -m swagger_server

A message will be displayed as
	`` * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)``


Test on broswer or make curl calls to test
	 
     curl http://localhost:8080/cloudmesh/file-system/S3/listData
     curl http://localhost:8080/cloudmesh/file-system/drive/listData
     curl http://localhost:8080/cloudmesh/file-system/VM/listData

These calls will list all data in Amazon S3, Google drive and Virtual machine respectively
#### Output

Video to display working of this project 
	
<https://drive.google.com/file/d/11FCSg7vU61l9Mm6_M4P1JJxVi62Yn5f1/view>

Docker implementation with no data in config.yaml file 

<https://drive.google.com/file/d/1L0dJSE4IQ0RI2_wcI4UTIxAKEyxSPs2K/view>


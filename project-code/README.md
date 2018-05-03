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



## Test

To test the service follw these steps

### 1. Using swagger code generator

To use Abstract File System, below python libraries needs to be installed

* pip install boto3
* pip install pyyaml
* pip install --upgrade google-api-python-client


Follow these steps to run Abstract File System project

* Clone repository ``hid-sp18-420.git``
* Go to folder ``/project-code``
* Download swagger-codegen-cli jar file by command

        wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar

* run command 	

        java -jar swagger-codegen-cli-2.3.1.jar generate  -i abstractFileSystem.yaml  -l python-flask  -o server/file-system/flaskConnexion  -D supportPython2=true 

This will generate server stubs

* copy all_drive_operations_controller.py, all_s3_operations_controller.py and all_vm_operations_controller.py files to ``/server/file-system/flaskConnexion/swagger_server/controllers``
* go to ``cd server/file-system/flaskConnexion``
* run ``pip install -r requirements.txt``
* run ``python setup.py install``
* run ``python -m swagger_server``
* A message will be displayed as
	`` * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)``

* Test on broswer or make curl calls to test
	 
     curl http://localhost:8080/cloudmesh/file-system/S3/listData
     curl http://localhost:8080/cloudmesh/file-system/drive/listData
     curl http://localhost:8080/cloudmesh/file-system/VM/listData

These calls will list all data in Amazon S3, Google drive and Virtual machine respectively



### 2. Using make file

Clone repository ``hid-sp18-420.git``

Go to folder ``/project-code``

Use command ``make`` to generate code 

Use command ``make test`` to test the code

Use command ``make clean`` to clean the code

### 3. Using Docker

Clone repository ``hid-sp18-420.git``

Go to folder ``/project-code``

Use command ``make container``

This will internally call ``make docker-build`` and ``make docker-start``

Once docker build is successful and container is created, run

    make test

to check the services. Run

    make docker-clean

to remove docker image


#### Output

Video to display working of this project 
	
<https://drive.google.com/open?id=1wBY0_yscvKAm8VPwd87DSElqNchx8b2z>

Docker implementation without config.yaml file 

<https://drive.google.com/open?id=1k9WgpiZ8oT4IYo9ts0dJ7mQbyCH8O-XX>






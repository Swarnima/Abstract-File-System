# Cloud and Big Data Rest Service with Swagger

## Implemented for Amazon S3

hid-sp18-420

Below operations are performed on Amazon S3 using Rest Service with swagger
1. Get list of all buckets
2. Get list of all objects in a given bucket

### Setup
I have used amazon.yaml to write the swagger specification and used swagger-codegen-cli-2.3.1.jar to generate the services

Main functionality can be found in below files-
1. Get list of all buckets

    hid-sp18-420/swagger/server/amazon/flaskConnection/swagger_server/controllers/list_buckets_controller.py

2. Get list of all objects in a given bucket

    hid-sp18-420/swagger/server/amazon/flaskConnection/swagger_server/controllers/default_controller.py

### Test

#### 1. Using swagger code generator

* Clone repository ``hid-sp18-420.git``
* Go to folder ``/server/cpu/flaskConnexion``
* Download swagger-codegen-cli jar file by command
	``wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
``
* run command 	
``java -jar swagger-codegen-cli-2.3.1.jar generate  -i amazon.yaml  -l python-flask  -o server/amazonS3/flaskConnexion  -D supportPython2=true ``
	
	 This will generate server stubs
* copy list_buckets_controller.py and default_controller.py files to ``/server/amazonS3/flaskConnexion/swagger_server/controllers``
* go to ``cd swagger_example/client/cpu``
* run ``pip install -r requirements.txt``
* run ``python setup.py install``
* run ``python -m swagger_server``
* A message will be displayed as
	`` * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)``

* Test on broswer or make curl calls to test

	url http://localhost:8080/cloudmesh/amazonS3/listBuckets
	curl http://localhost:8080/cloudmesh/amazonS3/listObjects/spring-18
	curl http://localhost:8080/cloudmesh/amazonS3/listObjects/test-cloudmesh
	curl http://localhost:8080/cloudmesh/amazonS3/listObjects/hid-420


#### 2. Using make file

Use command ``make`` to generate code 

Use command ``make test`` to test the code

Use command ``make clean`` to clean the code

#### 3. Using Docker

Use command ``make container``

This will internally call ``make docker-build`` and ``make docker-start``

Once docker build is successful and container is created, run ``make test`` to check the services.

Run ``make docker-clean`` to remove docker image

 


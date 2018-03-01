# Cloud and Big Data Rest Service with Swagger

## Implemented for Amazon S3

Below operations are performed on Amazon S3 using Rest Service with swagger
1. Get list of all buckets
2. Get list of all objects in a given bucket

I have used amazon.yaml to write the swagger specification and used swagger-codegen-cli-2.3.1.jar to generate the services

Main functionality can be found in below files-
1. Get list of all buckets

    hid-sp18-420/swagger/server/amazon/flaskConnection/swagger_server/controllers/list_buckets_controller.py

2. Get list of all objects in a given bucket

    hid-sp18-420/swagger/server/amazon/flaskConnection/swagger_server/controllers/default_controller.py



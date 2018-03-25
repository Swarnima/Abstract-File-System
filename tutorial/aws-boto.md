# AWS Boto 

hid-sp18-420

Boto is a software development kit (SDK) that provides AWS interface for Python applications. Boto versions include Boto, Boto3 and Botocore. Boto3 is the latest version of the SDK which supports Python versions 2.6.5, 2.7 and 3.3. 

Boto supports different AWS services such as, Elastic Compute Cloud (EC2), DynamoDB, AWS Config, CloudWatch and Simple Storage Service (S3).


## Boto Installation


To install boto with its latest release, use command – 
	
    pip install boto

To install boto from source, use command –

	git clone git://github.com/boto/boto.git
	cd boto
	python setup.py install

To install additional modules to use boto.cloudsearch, boto.manage, boto.mashups and to get all modules required for test suite, run command – 

	python setup.py install

## EC2 interface of Boto

####  Create connection 

To access EC2 instance, first import the required package.

	import boto.ec2

Make a connection to from application by specifying AWS region in which the user account is created, aws access key and secret key. AWS provides access key and secret key when a new user is created. Access key and secret key helps to identify the user. 

	connection = boto.ec2.connect_to_region('<region name>', aws_access_key_id = '<access key>', aws_secret_access_key = '<secret key'>)

connection object now points to EC2Connection object returned by function connect_to_region. 

#### Launch a new instance

To launch a new instance with default properties

	connection.run_instances('<ami-id>')

Additional parameters can be specified to create instance of specific type and security group. 

	connection.run_instances('<ami-id>',key_name='<key>', instance_type='<type>',      security_groups=['<security group list>'])

Instance type specifies the storage and type of platform. Secutity groups are required to provide access rights such as access to SSH into  the instance. 

#### Check running instances
get_all_reservations function of EC2Connection object will return list of running instances. 

	reservations = connection.get_all_reservations()
	instances = reservations[0].instances



#### Stop instance

Up and running instances can be stopped. stop_instances function of connection object enables multiple instances to be stopped in one command. 

    connection.stop_instances(instance_ids=['<id1>','<id2>', ...]) 
    

#### Terminate instance

To terminate one or more instances simultaneously, use terminate_instances function. 

	connection.terminate_instances(instance_ids=['<id1>','<id2>', ..]) 



## Amazon S3 interface of Boto


####  Create connection 

Import required packages

	import boto.s3
	from boto.s3.key import Key

Create a connection 

	connection = boto.connect_s3('<access-key>','<secret-key>')
    


#### Create new bucket in S3
Amazon S3 stores all its data in Bucket. There is no limitation specified by AWS about number of data files allowed per bucket. 

Bucket name has to be unique name accross all the AWS regions and hence globally unique. 

	bucket = conn.create_bucket('<bucket_name>')

If bucket name is unique, a new bucket of specified name will get created.
If bucket name is not unique, application will throw error as

	boto.exception.S3CreateError: S3Error[409]: Conflict


#### Upload data

To upload a file in the S3 bucket, first create a key object from new_key() function of bucket. 

	key = bucket.new_key('hello2.txt')
	key.set_contents_from_string('Hello World!')

This will create hello.txt file with content Hello World! in the text file. This file can be found inside the bucket in which new key is created. 


#### List all buckets

One account can have maximum 100 buckets in which data objects can be stored. 

	result = connection.get_all_buckets()

get_all_buckets function of S3Connection lists all the buckets within account. It returns ResultSet object which has list of all buckets.
    
 

#### List all objects in a bucket

Data objects stored in a bucket has a metadata associated with it such as LastModified date and time. This information can also be captured. 

	for key in bucket.list():
        print "{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                )



#### Delete object

To delete any data object from bucket, delete_key function of bucket is used. 

	k = Key(<bucket-name>, <file-name>)
	k.delete()

#### Delete bucket

To delete a bucket, provide a bucket name and call delete_bucket function of S3Connection object. 

	connection.delete_bucket('<bucket-name>') 



# AWS Account Application 

hid-sp18-420

Amazon Web Service (AWS) is a cloud computing platform provided by
Amazon.  To access any AWS service, it is mandatory to create an account
with AWS. This account can be a free account or a regular
account depending upon the service usage.
AWS free tier provides 12 months of introductory period to
use AWS services for free with some limitations on usage.

## Steps to create new account

### Step 1 : Go to website

Open https://www.aws.com/, and click on Create New Account

### Step 2: AWS Account details

Fill in all the details such as email address, password, confirm the
password and AWS account name. The AWS account name can be changed
later if required.  Click on Continue.

![AWS Account details](https://github.com/cloudmesh-community/hid-sp18-420/blob/master/tutorial/images/aws%20step%202.jpg?raw=true)


### Step 3: Contact information

Fill out the contact information.

Select the account type as Professional or Personal. (Account creation
steps are the same for both).
 
Provide all details such as Full Name, Company Name (Only for
Professional account), Phone Number, Country, Address, State, City,
and Postal code.

Before clicking on `Create Account and Continue`, go through the terms
and conditions and confirm the AWS Customer Agreement.

![AWS Contact Information](https://github.com/cloudmesh-community/hid-sp18-420/blob/master/tutorial/images/aws_account_step3.PNG?raw=true)


### Step 4: Payment Information

On the next page, AWS asks for a credit card or debit card
details. Payment information is required by AWS to verify the user
account creation. We do not recommend that you use a debit card.  Fill
in all valid details and click on `Secure Submit`. Validate the card
with a one time password or secured password.  It will charge a small
amount which is payed back once card is validated.

![AWS Payment Information](https://github.com/cloudmesh-community/hid-sp18-420/blob/master/tutorial/images/aws_account_payment.PNG?raw=true)


### Step 5: Phone verification

The next step is to verify phone number. 

On this page, give a valid phone number where calls can be received. 

Fill out a captcha and choose Call me now.

AWS will make a call on the given number and give a 4 digit code to verify
your phone number.

### Step 6: Select a support plan 

AWS offers 3 plans while creating an account

1. Basic Plan: This is a *free* plan which provides 24*7 availability of
   resources, best practices checks to improve secuirity and
   performance, and access to health status and notifications.
2. Developer plan: This plan costs from $29 per month which is used
   for development and testing.
3. Business plan: This plan costs from $100 per month which is used in
   case of production workloads and business critical dependencies.

### Account created successfully

Once a support plan is selected an account creation is complete. AWS
offers some 10 minutes videos to get an understanding of each AWS service.
These videos are available at https://aws.amazon.com/getting-started/tutorials/


## AWS Free Tier vs. Regular costing

AWS offers a 12 months of period to access AWS services for *free* with
limited access. If these limitations are crossed, AWS will charge for
those services and respective amonut will be deducted from the card
which was provided at the time of account creation. Thus it is
important to identify exactly what is included with the free offering.

#### Cost for AWS Services


- Amazon EC2:

	- AWS free tier offers 750 hours of Amazon EC2 Linux or Microsoft
      Windows server with t2.micro instance that is 1 GiB memory and
      32-bit or 64-bit platform.
	- AWS EC2 Regular costing varies based on the region (AWS region
      is nothing but the area specified by AWS for their resources)
      and type of service.
    - For general purpose t2.micro linux machine 
      with 1GiB memory and 32-bit or 64-bit
      platform costs $0.0116 per Hour in US region.
        
- Amazon Simple Storage Service (S3)

	- AWS free tier offers 5 GB of standard storage, 20000 requests to
      get data, and 2000 requests to put data.
	- AWS S3 Regular costing varies based on AWS region and storage.
    - Standard storage of over 500 TB per month costs for $0.021 per GB in US region.

- Amazon Relational Database Service (RDS)

	- AWS free tier provides 750 hours of Amazon RDS t2.micro instance
      with 20 GB database storage, 10 millions IOs and 20 GB backup
      storage. RDS can run MySQL, PostgreSQL, MariaDB, Oracle BYOL or
      SQL Server.
	- RDS regular costing varies based on AWS region and database
      type.
    - For RDS with t2.micro instance in US region costs for $0.017 per hour.

- Amazon API Gateway 

	- AWS free tier offers 1 million API calls per month are free
	- Regular costing for API Gateway varies based on AWS region. 
    - For US region, $3.50 per million API calls are charged. 
    
- Data transfer
	
    - AWS supports 15 GB of data transfer out for free tier usage
    - Regular data transfer cost for US region is $0.09/GB for
      the first 10 TB then $0.085/GB for the next 40 TB then $0.07/GB
      for the next 100 TB and $0.05/GB for the next 350 TB.


## References
 
* <https://aws.amazon.com/free/>
* <https://aws.amazon.com/ec2/pricing/on-demand/>
* <https://aws.amazon.com/s3/pricing/>
* <https://aws.amazon.com/rds/pricing/>
* <https://aws.amazon.com/api-gateway/pricing/>

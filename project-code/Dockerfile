FROM ubuntu:16.04
MAINTAINER swarnima <shsowani@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    git-core \
    wget \
    curl \
    default-jre \
    libssl-dev -y

# install net tools
RUN pip install --upgrade pip
RUN pip install boto
RUN pip install pyyaml
RUN pip install --upgrade google-api-python-client
    
#RUN apt-get update -q && apt-get install -qy default-jre 

RUN git clone https://github.com/cloudmesh-community/hid-sp18-420.git

WORKDIR /hid-sp18-420/project-code

#RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
EXPOSE 8080

#FROM openjdk:7 
RUN make service

CMD ["make", "start"]

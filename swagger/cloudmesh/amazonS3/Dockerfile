FROM ubuntu:16.04
MAINTAINER Swarnima Sowani <shsownai@iu.edu>

RUN apt-get update -q && apt-get install -qy \
    build-essential \
    python-dev \
    python-pip \
    #libssl-dev \
    #zlib1g-dev \
    #libbz2-dev \
    #libreadline-dev \
    #libsqlite3-dev \
    #pandoc \
    wget \
    curl \
    #emacs \
    git-core \
    default-jre \
	software-properties-common -y

# install net tools
RUN apt-get install -q -y net-tools

RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv

ENV HOME  /
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.6.2
RUN pyenv global 3.6.2
RUN python -m ensurepip
RUN pip install --upgrade pip
RUN pip install boto

RUN git clone https://github.com/cloudmesh-community/hid-sp18-420.git
WORKDIR /hid-sp18-420/swagger/cloudmesh/amazonS3

RUN wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar


EXPOSE 8080
RUN make service

CMD ["make", "start"]

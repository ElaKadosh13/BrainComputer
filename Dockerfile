FROM ubuntu:latest

#todo - check out in mazeget 9 shkufit 77 installs to docker image
RUN apt-get update \
  && apt-get install -y python3.8 python3-pip\
  && python3.8 -m pip install --upgrade pip setuptools wheel \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3.8 python \
  && python3.8 -m pip install --upgrade pip setuptools wheel

COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY braincomputer/ /braincomputer


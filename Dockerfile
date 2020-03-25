FROM ubuntu:latest

LABEL version="1.0"
LABEL maintainer="Platforme <development@platforme.com>"

EXPOSE 8080

ENV LEVEL INFO
ENV SERVER netius
ENV SERVER_ENCODING gzip
ENV HOST 0.0.0.0
ENV PORT 8080
ENV PYTHONPATH /src

ADD requirements.txt /
ADD extra.txt /
ADD src /src

RUN apt-get update && apt-get install -y -q python python-setuptools python-dev python-pip
RUN pip install -r /requirements.txt && pip install -r /extra.txt && pip install --upgrade netius

CMD ["/usr/bin/python", "/src/ripe_skeleton/main.py"]

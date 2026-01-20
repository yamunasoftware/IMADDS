FROM python:3.10-slim
WORKDIR /main
USER root
RUN mkdir /main/src
RUN mkdir /main/check

COPY requirements.txt /main/
RUN apt-get update && apt-get install -y dos2unix
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install --no-cache-dir -r requirements.txt
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY lib/. /main/lib
COPY src/. /main/src
COPY run.sh /main/
RUN dos2unix /main/*
CMD ["bash", "-c", "sleep 10 && bash run.sh"]
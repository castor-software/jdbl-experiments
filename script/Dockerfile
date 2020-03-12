FROM maven:3-jdk-8

RUN apt-get update
RUN apt-get install -y python3 python3-pip git

RUN git clone https://github.com/castor-software/jdbl.git
RUN cd jdbl; mvn install -Dmaven.test.skip;

COPY requirements.txt /requirements.txt
RUN pip3 install --requirement requirements.txt 

RUN mkdir /results
ENV M2_HOME=/root/.m2/

COPY __init__.py /__init__.py
COPY jdbl.py /jdbl.py
COPY core /core


ENTRYPOINT [ "./jdbl.py" ]
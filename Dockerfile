FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip

COPY src/main.py /src/
COPY src/utils/twitter_handler.py /src/utils/
COPY src/utils/tweets.json /src/utils/
COPY src/utils/money_api.py /src/utils/
COPY src/utils/auth_tokens.py /src/utils/
COPY requirements.txt /tmp

RUN apt-get update
RUN apt-get install cron

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /
CMD ["python3", "src/main.py"]
FROM python:3

COPY src/main.py /src/
COPY src/utils/twitter_handler.py /src/utils/
COPY src/utils/tweets.json /src/utils/
COPY src/utils/money_api.py /src/utils/
COPY src/utils/auth_tokens.py /src/utils/
COPY requirements.txt /tmp

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /src
CMD ["python3", "main.py"]
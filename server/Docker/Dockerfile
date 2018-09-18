FROM Python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /language_startup
WORKDIR /language_startup

COPY . /language_startup/

RUN pip install -r requirements.txt
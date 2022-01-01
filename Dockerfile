FROM python:3.7-alpine
MAINTAINER NRC

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r ./requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

ENTRYPOINT ["python"]

RUN adduser -D user
USER user



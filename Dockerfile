FROM python:3.8.5-slim-buster as base

RUN pip install testinfra==5.2.2

ENTRYPOINT ["pytest"]

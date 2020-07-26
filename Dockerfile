FROM python:3.8.5-slim-buster as base

RUN pip install testinfra==5.2.2

CMD ["pytest"]

# -------------------------- #
#           TESTS            #
# -------------------------- #

FROM base as test-build

ARG DOCKER_TEST_DIR=./docker/test

RUN mkdir -p $DOCKER_TEST_DIR

WORKDIR $DOCKER_TEST_DIR

COPY ./test .

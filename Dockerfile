FROM python:3.7-alpine

COPY . /common-words/app
WORKDIR /common-words/app
RUN pip install -r requirements.txt

# Run unit tests with coverage


# Run processing
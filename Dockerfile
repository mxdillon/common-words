FROM python:3.7-slim

# Copy and install requirements first to take advantage of caching.
COPY requirements.txt /common-words/app/
RUN pip install -r /common-words/app/requirements.txt

# Copy rest of files; set workdir
COPY . /common-words/app
WORKDIR /common-words/app

# Run unit tests with coverage. Build fails if coverage floor not met.
RUN python3 -m pytest --cov ./src/ --cov-fail-under=85

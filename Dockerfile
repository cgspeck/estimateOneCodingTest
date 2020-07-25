FROM python:3

WORKDIR /usr/src/app

COPY requirements* ./

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

RUN pip install -e .[dev]

FROM python:3.7.4

RUN mkdir /canvas
WORKDIR /canvas

COPY requirements.txt /canvas
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /canvas

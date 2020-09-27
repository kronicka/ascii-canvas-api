FROM python:3.7.4

RUN mkdir /canvas
WORKDIR /canvas

COPY requirements.txt /canvas
RUN pip install --upgrade pip && pip install virtualenv
RUN virtualenv venv
RUN . venv/bin/activate
RUN pip install -r requirements.txt
COPY . /canvas

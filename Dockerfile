FROM python:3

WORKDIR /lms

COPY ./requirements.txt /lms/

RUN pip install -r requirements.txt

COPY . .

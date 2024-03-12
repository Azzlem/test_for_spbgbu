FROM python:3.11

LABEL authors="azzlem"

WORKDIR /app

COPY ./requirement.txt .

RUN pip install -r requirement.txt

COPY . .
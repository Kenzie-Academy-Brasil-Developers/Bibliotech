FROM python:3.10

RUN apt update
RUN apt upgrade -y

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt .

RUN pip install -r /app/requirements.txt

COPY . .
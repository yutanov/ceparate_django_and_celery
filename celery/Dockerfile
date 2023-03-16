FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /celery
COPY . /celery/
WORKDIR /celery

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


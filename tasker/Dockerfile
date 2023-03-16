FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /tasker
COPY . /tasker/
WORKDIR /tasker

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


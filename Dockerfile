FROM python:2.7
ENV APP_PORT 5000
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD ./app/ /app/

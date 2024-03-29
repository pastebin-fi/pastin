FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
COPY ./defconfig.ini /app/config.ini

COPY ./nginx.conf /etc/nginx
RUN chmod +x ./start.sh

EXPOSE 80

RUN apt-get -y remove python3-dev build-essential

CMD ["./start.sh"]

FROM python:3.8.5-buster

WORKDIR /usr/src/app

COPY . .

CMD [ "python", "./main.py" ]
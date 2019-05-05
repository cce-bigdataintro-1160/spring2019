FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install python3

COPY stock_price.py .

CMD ["python3","-u","stock_price.py"]

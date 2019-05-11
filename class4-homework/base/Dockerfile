FROM ubuntu:16.04

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip

RUN pip3 install numpy pandas argparse matplotlib seaborn plotly sklearn

WORKDIR /app

COPY "my_csv_reader.py" /app
COPY "housing.data" /app

CMD ["python3","-u","./my_csv_reader.py"]
docker build -t my_csv_reader_adv_reach:latest .
docker run my_csv_reader_adv_reach:latest "housing.data" "housing.names" "\s+"
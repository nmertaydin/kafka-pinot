# Using Apache Pinot as a Kafka Consumer and Data Storage for Fast On-the-Fly Aggregations

This is a PoC I prepared to demonstrate positioning Apache Pinot as a Kafka consumer and data storage to enable fast on-the-fly aggregations.

[Here]() is my post about this PoC.

### The Ingredients

- Source database
- Message broker
- Destination (consumer)

### Technologies Used

- Kafka
- Pinot
- Python

### To Run

Open up a terminal and browse to the cloned folder and execute the following command to see the magic happen:

`docker-compose up`

Or to have everything run at the background silently, add -d

`docker-compose up -d`

Open another terminal and execute a script to create table in Apache Pinot:

`./run.sh`

Browse Apache Pinot UI to query some data

http://localhost:9000/#/query

Execute the following SQL repeatedly to see the sample on-the-fly aggregation results:
> SELECT person_name, sum(incoming_amount) FROM poc
GROUP BY person_name
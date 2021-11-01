CREATE KEYSPACE wallet WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE wallet.user (
   userId uuid,
   name varchar,
   email varchar,
   PRIMARY KEY (userId)
);

CREATE TABLE wallet.addresses (
   userId uuid,
   address varchar,
   PRIMARY KEY ((userId), address)
);

CREATE TABLE wallet.transaction (
   timestamp double,
   transactionId uuid,
   address varchar,
   amount double,
   type varchar,
   coin varchar,
   PRIMARY KEY (address, timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);


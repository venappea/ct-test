# Project Setup

Preinstallation: 

- Must have docker installed [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
- Python38
- 

```bash
# setup
## Start by launching the cassandra container (this is our db)
docker build -f Dockerfile.db -t my-cassandra .

## Due to some issues, having issues building the container so we will do a manually launching
## of the container. This will let us login to the actual container
docker run -p 9042:9042 -it my-cassandra /bin/bash

## At this point, you're inside the connect so run the following command 
root@fdb7153b3bb2:/# ls
bin   dev                         docker-entrypoint.sh  etc   lib    mnt  patched-entrypoint.sh  root  run-init-scripts.sh  srv  tmp  var
boot  docker-entrypoint-initdb.d  entrypoint.sh         home  media  opt  proc                   run   sbin                 sys  usr
root@fdb7153b3bb2:/# **./entrypoint.sh**

## This will setup the db. Launch another terminal. 
# In the new terminal execute python app.py Thsi will launch our backend service locally
## the commands below can be used to actually add items to our database
(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % python app.py
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://10.0.0.126:5000/ (Press CTRL+C to quit)

## curl commands to populate database

## Adding a transaction
curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_1", "amount": "5.0", "coin": "BTC", "type": "out"}' http://10.0.0.126:5000//v1/transaction/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_1", "amount": "3.0", "coin": "BTC", "type": "out"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 203
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:29:46 GMT

{
  "current_time": "2021-10-31 19:29:46.388080", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "Successfully added new transaction. TransactionId: c0e4a039-257c-4bca-8cfd-369232bdb04f"
}

## getting a transaction
curl -i -H "Content-Type: application/json" -X GET -d '{"address":"wallet_1"}' http://10.0.0.126:5000//v1/transaction/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X GET -d '{"address":"wallet_1"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 400
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:35:15 GMT

{
  "current_time": "2021-10-31 19:35:15.112882", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "[\"timestamp:1635733786.374988 transaction_id: c0e4a039-257c-4bca-8cfd-369232bdb04f & address: wallet_1 amount: 3.0 & type: out & coin: BTC\", \"timestamp:1635733754.052385 transaction_id: 05784e3f-3f9a-472d-b33d-16f03bdc36c4 & address: wallet_1 amount: 5.0 & type: out & coin: BTC\"]"
}

## adding a wallet for a user
curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1", "address":"wallet_1"}' http://10.0.0.126:5000//v1/wallet/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1", "address":"wallet_1"}' http://10.0.0.126:5000//v1/wallet/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 145
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:25:00 GMT

{
  "current_time": "2021-10-31 19:25:00.845143", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "Successfully added new wallet"
}

## Getting a wallet for a user
curl -i -H "Content-Type: application/json" -X GET -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1"}' http://10.0.0.126:5000//v1/wallet/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X GET -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1"}' http://10.0.0.126:5000//v1/wallet/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 211
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:28:15 GMT

{
  "current_time": "2021-10-31 19:28:15.932829", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "UserId:c5fbb139-bf50-483e-af92-ebe3b2d461b1 and addresses: ['wallet_1', 'wallet_2', 'wallet_3']"
}

## Adding a user
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Ven", "email": "ven@gmail.com"}' [http://10.0.0.126:5000//v1/](http://10.0.0.126:5000//v1/wallet/)user/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"name":"Ven", "email": "ven@gmail.com"}' http://10.0.0.126:5000//v1/user/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 189
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:22:55 GMT

{
  "current_time": "2021-10-31 19:22:55.370086", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "Successfully added new user. userId: c5fbb139-bf50-483e-af92-ebe3b2d461b1"
}

## Getting a user
curl -i -H "Content-Type: application/json" -X GET -d '{"user_id": "c5fbb139-bf50-483e-af92-ebe3b2d461b1"}' http://10.0.0.126:5000//v1/user/

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X GET -d '{"user_id": "c5fbb139-bf50-483e-af92-ebe3b2d461b1"}' http://10.0.0.126:5000//v1/user/
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 195
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 02:24:05 GMT

{
  "current_time": "2021-10-31 19:24:05.600229", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "UserId:c5fbb139-bf50-483e-af92-ebe3b2d461b1  & name: Ven & email: ven@gmail.com"
}
```

## Testing example for transaction detector
```bash
## Add the user

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X 
POST -d '{"name":"Ven", "email": "ven@gmail.com"}' http://10.0.0.126:5000//v1/user/
HTTP/1.0 200 OK

## Add wallets to the user (wallet_1, wallet_2, wallet_3)

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1", "address":"wallet_1"}' http://10.0.0.126:5000//v1/wallet/
HTTP/1.0 200 OK

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1", "address":"wallet_2"}' http://10.0.0.126:5000//v1/wallet/
HTTP/1.0 200 OK

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1", "address":"wallet_3"}' http://10.0.0.126:5000//v1/wallet/
HTTP/1.0 200 OK

## Add transactions to the user (same transactions as in the example)

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_1", "amount": "5.0", "coin": "BTC", "type": "out"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_1", "amount": "3.0", "coin": "BTC", "type": "out"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_2", "amount": "5.0", "coin": "BTC", "type": "in"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK

(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X POST -d '{"address":"wallet_3", "amount": "5.0", "coin": "BTC", "type": "in"}' http://10.0.0.126:5000//v1/transaction/
HTTP/1.0 200 OK
Content-Type: application/json

## now you can invoke the endpoint to get the filtered transactions
(venv) venkateshappea@Venkateshs-MacBook-Air docker_flask_cassandra_example-master % curl -i -H "Content-Type: application/json" -X GET -d '{"userId":"c5fbb139-bf50-483e-af92-ebe3b2d461b1"}' http://10.0.0.126:5000//v1/user/transaction
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 369
Server: Werkzeug/2.0.2 Python/3.8.2
Date: Mon, 01 Nov 2021 04:13:26 GMT

{
  "current_time": "2021-10-31 21:13:26.921618", 
  "hostname": "Venkateshs-MacBook-Air.local", 
  "message": "Transactions for user_id c5fbb139-bf50-483e-af92-ebe3b2d461b1 is [(UUID('05784e3f-3f9a-472d-b33d-16f03bdc36c4'), UUID('1875a96e-2e3e-4d05-a091-4ec4ec9ce2c8')), (UUID('05784e3f-3f9a-472d-b33d-16f03bdc36c4'), UUID('1875a96e-2e3e-4d05-a091-4ec4ec9ce2c8'))]"
}
```

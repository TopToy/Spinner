# Spinner
A front end RESTFul server for negotiating TopToy 

## Getting Started
Spinner is supported only on an Ubuntu linux machine

### Prerequisites
1. Install Python3.7
    ```bash
       sudo apt-get update
       sudo apt-get install python3.7
    ```
1. Install pip3
    ```bash
       sudo apt-get install python3-pip
    ```
1. Install necessary packages
    ```bash
       make install
    ```
    
Finally build the project
```bash
make build
```

## Run a Spinner Server
1. Go to `src/settings.py` and set `TOPTOY_IP` to be the string ip of your `TOP` server.
Note that currently `TOP` listen to an RPC request on port `9876` only. 

1. Go to `src/settings.py` and set `SPINNER_IP` to be the string ip of the `SPINNER` server.
In addition, change `SPINNER_PORT` to the port on which `SPINNER` is listen on.

## Requests Specification
Spinner supports the following requests:

Method | URL | Parameters | Description | Returned Data format  
-------|-----|------------|-------------|---------------------
GET | `toptoy/` | None | Returns a general information about Spinner | Text
GET | `toptoy/state/height` | None | Returns the number of blocks in the blockchain | Json
GET | `toptoy/state/liveness`| None | Returns if the TOP server has responded | Text
GET | `toptoy/state/pool_size` | None | Returns the number of transactions that were not proposed yet | Json
GET | `toptoy/state/pending_size` | None | Returns the number of transactions that have been proposed but not yet decided | Json
GET | `toptoy/state/validators` | None | Returns a list of the validators IPs | Json
GET | `toptoy/state/info` | None | Returns a general info about the TOP cluster deployment | Json
GET | `transactions/cid=<clientID>&worker=<channel>&pid=<proposerID>&bid=<bid>&tx_num=<txNum>&blocking=blocking` | <ul><li>cid stands for the REST client ID</li><li>worker, pid, bid, and tx_num form a transaction ID and retrieved by submitting a transaction</li><li>blocking indicates weather to block the call id the transaction has not been decided yet</li></ul> | Return the desired transaction | Json  
GET | `transactions/cid=<clientID>&worker=<channel>&pid=<proposerID>&bid=<bid>&tx_num=<txNum>/status` | <ul><li>cid stands for the REST client ID</li><li>worker, pid, bid, and tx_num form a transaction ID and retrieved by submitting a transaction</li></li></ul> | Return the transaction status (0 if unknown) | Json  
GET | `blocks/cid=<clientID>&height=<height>&blocking=<blocking>` | <ul><li>cid stands for the REST client ID</li><li>height indicated the index of the block in the chain</li><li>blocking indicates weather to block the call id the block has not been decided yet</li> | Returns the desired block | Json
POST | `transactions/cid=<clientID>/write` | <ul><li>cid stands for the requester ID</li><The body request contains the data in a string format</li></ul>| Submit a new transaction and returns the transaction ID | Json
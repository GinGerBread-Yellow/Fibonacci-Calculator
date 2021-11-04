# Fibonacci-Calculator

## Environment
- python 3.7.1
## How to run
- Install project dependencies
```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install grpc packages
$ pip3 install -r requirements.txt
```
- Compile protobuf schema to python wrapper
```bash
$ cd rest_server && make
$ cd fib_server && make
```
- Start the gRPC service
```bash
$ cd fib_server
$ python3 server.py --ip 0.0.0.0 --port 8080
```
- Start the REST server
```bash
# You will get 55 value computed by the grpc service
$ cd rest_server 
$ python3 manage.py migrate
$ python3 manage.py runserver
```

- To test POST method
```bash
# $(Number) is the input
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/rest/fibonacci/ -d "{\"order\":\"$(Number)\"}"
'''
and you shold get
{
    "status":"success",
    "data":
    {
        "id":1,
        "order":10
        "value":55
    }
}
'''
```
- To test GET method
```bash
$ curl http://localhost:8000/rest/logs
'''
and you should get
{
    "status":"success",
    "history":
    [
        {
            "id":1,
            "order":10
            "value":55
        },
        {
            "id":2,
            "order":12
            "value":144
        },
        {
            "id":3,
            "order":1
            "value":1
        }
    ]
}
```

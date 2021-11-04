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
$ make
```
- Start the gRPC service
```bash
$ python3 server.py --ip 0.0.0.0 --port 8080
```
- Start the gRPC client
```bash
# You will get 55 value computed by the grpc service
$ python3 client.py --ip localhost --port 8080 --order 10
```

- To test POST method
```bash
# You will get 55
$ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8000/rest/fibonacci/ -d "{\"order\":\"10\"}"
'''
and you shold get
{
    "status":"success",
    "data":
    {
        "id":1,
        "order":10
    }
}
'''
```
- To test GET method
```bash
$ curl http://localhost:8000/rest/logs
```

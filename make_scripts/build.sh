#!/usr/bin/env bash

#pip install protobuf
#pip install grpcio-tools
#pip install grpcio
#pip install django
#pip install djangorestframework

protoc --proto_path=proto --python_out=src/proto proto/**/*.proto
python -m grpc_tools.protoc --proto_path=proto --python_out=src/proto --grpc_python_out=src/proto proto/crpcs/*.proto
#!/usr/bin/env bash

protoc --proto_path=proto --python_out=src proto/**/*.proto
python -m grpc_tools.protoc --proto_path=proto --python_out=src --grpc_python_out=src proto/crpcs/*.proto
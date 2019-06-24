#!/usr/bin/env bash

protoc --proto_path=proto --python_out=src/proto proto/**/*.proto
python -m grpc_tools.protoc --proto_path=proto --python_out=src/proto --grpc_python_out=src/proto proto/crpcs/*.proto
#!/usr/bin/env bash

protoc --proto_path=proto --python_out=src/proto proto/**/*.proto
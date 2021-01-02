## compile

```bash
pip install grpcio grpcio-tools
cd proto
python -m grpc_tools.protoc -I./ --python_out=../ --grpc_python_out=../ mail.proto

```

## run

1. `python server.py`
2. `python client.py`

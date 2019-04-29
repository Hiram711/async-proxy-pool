#! /bin/bash
nohup python -u client.py > nohup.out 2>&1 &
nohup python -u server_sanic.py > nohup.out 2>&1 &

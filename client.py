#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process
from async_proxy_pool.scheduler import run_schedule
from async_proxy_pool.webapi_sanic import app
from async_proxy_pool.config import SERVER_HOST, SERVER_PORT, SERVER_ACCESS_LOG


def run():
    api_process = Process(target=app.run, kwargs=dict(host=SERVER_HOST, port=SERVER_PORT, access_log=SERVER_ACCESS_LOG))
    api_process.start()
    generator_process = Process(target=run_schedule)
    generator_process.start()


if __name__ == '__main__':
    run()

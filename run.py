#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Process
from async_proxy_pool.scheduler import run_schedule
from async_proxy_pool.webapi_sanic import app
# from async_proxy_pool.webapi_flask import app
from async_proxy_pool.config import SERVER_HOST, SERVER_PORT, SERVER_ACCESS_LOG


class Runner:
    @staticmethod
    def crawl_and_validate():
        run_schedule()

    @staticmethod
    def api():
        app.run(host=SERVER_HOST, port=SERVER_PORT, access_log=SERVER_ACCESS_LOG)
        # app.run(host=SERVER_HOST, port=SERVER_PORT, debug=SERVER_ACCESS_LOG)

    def run(self):
        api_process = Process(target=Runner.api)
        api_process.start()
        worker_process = Process(target=Runner.crawl_and_validate)
        worker_process.start()


if __name__ == '__main__':
    r = Runner()
    r.run()

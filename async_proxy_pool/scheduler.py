#!/usr/bin/env python
# coding=utf-8

import time
from multiprocessing import Process

from async_proxy_pool.config import SERVER_HOST, SERVER_PORT, SERVER_ACCESS_LOG
from async_proxy_pool.webapi_sanic import app
from async_proxy_pool.logger import logger
from .config import CRAWLER_RUN_CYCLE, VALIDATOR_RUN_CYCLE
from .crawler import crawler
from .validator import validator


class Scheduler:
    @staticmethod
    def api():
        app.run(host=SERVER_HOST, port=SERVER_PORT, access_log=SERVER_ACCESS_LOG)

    @staticmethod
    def crawler_task(cycle=CRAWLER_RUN_CYCLE):
        while True:
            crawler.run()
            time.sleep(cycle * 60)

    @staticmethod
    def validator_task(cycle=VALIDATOR_RUN_CYCLE):
        while True:
            validator.run()
            time.sleep(cycle * 60)

    def run(self):
        try:
            api_process = Process(target=Scheduler.api)
            api_process.start()
            crawler_process = Process(target=Scheduler.crawler_task)
            crawler_process.start()
            validator_process = Process(target=Scheduler.validator_task)
            validator_process.start()
        except KeyboardInterrupt as e:
            logger.info("You have canceled all jobs")

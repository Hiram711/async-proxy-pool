#!/usr/bin/env python
# coding=utf-8

from sanic import Sanic
from sanic.response import json

from async_proxy_pool.database import redis_conn

app = Sanic()


@app.route("/")
async def test(request):
    return json({"Welcome": "This is a proxy pool system."})


@app.route("/pop")
async def pop_proxy(request):
    proxy = redis_conn.pop_proxy().decode("utf8")
    if proxy[:5] == "https":
        return json({"https": proxy})
    else:
        return json({"http": proxy})


@app.route("/get/<count:int>")
async def get(request, count):
    res = []
    for proxy in redis_conn.get_proxies(count):
        if proxy[:5] == "https":
            res.append({"https": proxy})
        else:
            res.append({"http": proxy})
    return json(res)


@app.route("/count")
async def count_proxies(request):
    count = redis_conn.count_proxies()
    return json({"count": str(count)})

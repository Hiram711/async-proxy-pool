FROM python:3.6
MAINTAINER Hiram <jie.zhang8@luckyair.net>

RUN mkdir /myapp
WORKDIR /myapp
COPY entrypoint.sh /myapp/
COPY run.py /myapp/
COPY requirements.txt /myapp/
COPY client.py /myapp/
COPY server_flask.py /myapp/
COPY server_sanic.py /myapp/
COPY async_proxy_pool /myapp/async_proxy_pool/
COPY test /myapp/test/

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

EXPOSE 3289

CMD ["/myapp/entrypoint.sh"]
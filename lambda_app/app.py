# -*- coding: utf-8 -*-

from chalice import Chalice
from loggerFactory.lbd import hello

app = Chalice(app_name="loggerFactory")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.high_level_api(event, context)

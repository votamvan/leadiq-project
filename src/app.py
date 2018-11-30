#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==================================================================== #
import logging
import falcon
from api import homepage

#init logging
log_file = "/opt/ml/log/server.log"
log_format = '%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger()
handler = logging.FileHandler(log_file, mode='w')
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

app = falcon.API()
app.add_route('/', homepage.HomePage())
logger.info("API server started")

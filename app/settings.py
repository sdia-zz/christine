#!/usr/bin/env python
#-*- coding:utf-8 -*-



import logging



PG_DATABASE = 'postgres'
PG_USER = 'postgres'
PG_PWD = 'postgres'
PG_HOST = 'localhost'
PG_PORT = 5432



log = logging.getLogger('christine')

logging_level = logging.DEBUG
logging_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s', '%Y-%m-%d %H:%M:%S')
to_console = logging.StreamHandler()
to_console.setLevel(logging_level)
to_console.setFormatter(logging_format)

log.addHandler(to_console)
log.setLevel(logging_level)

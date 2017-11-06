#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import json
import sqlapi


config = None
with open('config.json', 'r') as file:
    config = json.load(file)

sql = sqlapi.SqlApi(config['host'],
                    config['user'],
                    config['password'],
                    None)


request = None

#remove after finish
config['db'] = 'oui'


with open('create_db.sql', 'r') as file:
    request = file.read()


try:
    sql.send_request(request)
    sql.send_request('USE ' + config['db'])
except pymysql.err.InternalError as err:
    print(err)

print('Database "{}" created'.format(config['db']))


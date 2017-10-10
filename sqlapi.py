#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import pymysql as pysql
import pymysql.cursors as c


class SqlApi:

    """ Class allow to read and write mysql database. """
   
    """ Quick examples :

                # connection
        sql = SqlApi('localhost', 'username', 'password', 'db_name')

                # search request
        req = sql.select('my_table') + sql.where('my_field', "42")

                # insert request
        vals = ['biscuit', 'fraise', 'pomme', 'peche', 'chocolat', 'oreo']
        req = sql.insert('my_table', 'my_field', 'my_field_2', 'my_field_3') + sql.values(vals)"""

    def __init__(self, host, usr, pwd, db, charset='utf8mb4', cursor=c.DictCursor):
        self.connect = pysql.connect(host=host, user=usr, 
                                     password=pwd, db=db,
                                     charset=charset, cursorclass=cursor, 
                                     autocommit=True)
        
        self.sql = self.connect.cursor()
        self.number_field = 0

    def send_request(self,request):
        self.sql.execute(request)

    def add_quotes(self, element, *doublequotes):
        element = element.replace('"', "'")

        if(doublequotes):
            element = '"' + element + '"'
        else:
            element = "`" + element + "`"
        
        return element 

    def add_brackets(self, element):
        return ' (' + element + ')'


    def select(self, table):
        request = "SELECT * FROM " + self.add_quotes(table)
        return request

    def where(self, table, value):
        request = " WHERE " + self.add_quotes(table) + " = " + self.add_quotes(value,1)
        return request

    def insert(self, table, *field):
        self.number_field = len(field)
        table = self.add_quotes(table)
        field = ", ".join(field)
        field = self.add_brackets(field)

        request = "INSERT INTO " + table + field
        return request

    def values(self, val):

        values = [self.add_quotes(x,1) for x in val]

        if self.number_field and len(val) % self.number_field == 0:
            values = list(zip(*[iter(values)]*self.number_field))
            values = [self.add_brackets(", ".join(x)) for x in values]
            values = " VALUES" + ",".join(values) + ";"
        else:
            print('Erreur, valeurs manquantes dans vos champs')

        return values


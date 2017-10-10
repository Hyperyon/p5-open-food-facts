#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import urllib.request as get
import json
import pymysql as pysql
import pymysql.cursors as c

NUMBER_ITEMS_SHOWN = 20      # show how many category in terminal


class UserInterface:

    """This class manage interaction with user."""

    def __init__(self):
        self.userChoice = ''

    def showMenu(self):
        print('1. Chercher un meilleur produit')
        print('2. Consulter les produits sauvegardés')

    def getInputUser(self, mode):     # need to upgrade

        proceed = True
        while 'is not numeric choice' and proceed:
            self.userChoice = input('\nVotre choix : ')
            
            if self.userChoice.isnumeric():
                if mode == 'menu' and not 0 < int(self.userChoice) < 3:
                    print("Ce choix n'existe pas")
                elif mode == 'search' and not 0 < int(self.userChoice) < NUMBER_ITEMS_SHOWN+1 :
                    print("Ce choix n'existe pas")
                else:
                    proceed = False
            else:
                print('Veuillez saisir une valeur numérique')

        return int(self.userChoice)


class OpenFoodData:

    """Manage all interaction with database"""
    def __init__(self):
        pass


class SqlApi:

    """ Class allow to read and write mysql database  """

    def __init__(self, host, usr, pwd, db, charset='utf8mb4', cursor=c.DictCursor):
        self.connect = pysql.connect(host=host, user=usr, 
                                   password=pwd, db='OpenFoodFactsDb',
                                   charset=charset, cursorclass=cursor)
        
        self.sql = self.connect.cursor()
        self.number_field = 0


    def write_data(self, request):
        self.sql.execute(request)
        self.connect.commit()

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
        field = ", ".join(map(self.add_quotes, field))
        field = self.add_brackets(field)

        request = "INSERT INTO " + table + field
        return request

    def values(self, val):
        print(len(val))

        val = [self.add_quotes(x,1) for x in val]

        
        print(val)
        #return " VALUES" + val + ";"
        return ' toto'



sql = SqlApi('localhost', 'nico', 'password', 'OpenFoodData')
req = sql.select('ma_table') + sql.where('mon_champ', "j'esaais pas\"")


vals = ['blabla','dodo']
req = sql.insert('ma_table', 'champ1') + sql.values(vals)

print(req)


    

"""INSERT INTO `test` (`non`, `oui`) VALUES (`9`, `fdff`), (`7`, `dfsfsf`);"""


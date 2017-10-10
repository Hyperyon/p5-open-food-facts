#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import urllib.request as get
import json
import pymysql
import pymysql.cursors

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


class SqlRequest:

    """ Class allow to read and write mysql database  """

    def __init__(self):
        self.connexion = pymysql.connect(host='localhost',user='nico',password='password',
        db='OpenFoodFactsDb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        self.sql = self.connexion.cursor()
        self.categories = ''

    def write_data(self, request):
        self.sql.execute(request)
        self.connexion.commit()

    def search_data(self, request):

        main_category, specific_category = request

        start_req = "SELECT * FROM `products` "

        payload_req = "WHERE `specific_category` = "+ "'" + specific_category + "';"

        #payload_req = "WHERE `specific_category` = " + "'" + specific_category + "' "
        #payload_req += "AND `main_category` = "+ "'" + main_category + "';"

        req = start_req + payload_req

        print(req)
        self.sql.execute(req)

        [print(x,'\n\n') for x in self.sql]

    def get_categories(self):
        request = """SELECT * FROM `categories`"""
        self.sql.execute(request)
        self.categories = self.sql

        return self.categories.fetchmany(NUMBER_ITEMS_SHOWN)

    def get_one_category(self, category):
        category = "'" + category + "'"
        request = """SELECT * FROM `products` WHERE `main_category` = """ + category

        self.sql.execute(request)
        return self.sql.fetchmany(NUMBER_ITEMS_SHOWN)


sql = SqlRequest()
interface = UserInterface()

interface.showMenu()
answer = interface.getInputUser('menu')

if answer:      #check passed
    items = sql.get_categories()   # return list of dict

    for item in items:     # need to upgrade
        print(item['numero'], item['category'])

    choice = interface.getInputUser('search')


    choosen_category = items[choice-1]['category']
    result = sql.get_one_category(choosen_category)

    for index, element in enumerate(result):
        print(index+1, element['product_name'])

    choice = interface.getInputUser('search')
    result = result[choice-1]
    choosen_product = (result['product_name'], result['main_category'], result['specific_category'])

    sql.search_data(choosen_product[1:3])
    
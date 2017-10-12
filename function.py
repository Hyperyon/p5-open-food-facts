#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlapi

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

    def showData(self, items):
        for i, item in enumerate(items):
            print(i+1, item)


class OpenFoodData:

    """Manage all interaction with database. """

    def __init__(self):
        self.sql = sqlapi.SqlApi('localhost', 'nico', 'password', 'OpenFoodFactsDb')
        self.result = ''

    def save_product(self, request):
        pass
        #req = self.sql.insert()
        #req += self.sql.values()
        #self.sql.send_request()

    def search_products(self, choice):

        specific_category = self.result[choice-1]['specific_category']

        req = self.sql.select('products')
        req += self.sql.where('specific_category', specific_category)

        self.result = self.sql.send_request(req)

        #payload_req = "WHERE `specific_category` = " + "'" + specific_category + "' "
        #payload_req += "AND `main_category` = "+ "'" + main_category + "';"
    
        return [x['product_name'] for x in self.result]

    def get_categories(self):
        req = self.sql.select('categories')
        self.result = self.sql.send_request(req)

        self.result = [x['category'] for x in self.result]
        return self.result

    def get_one_category(self, choice):

        category = self.result[choice-1]

        req = self.sql.select('products')
        req += self.sql.where('main_category', category)

        self.result = self.sql.send_request(req)

        return [x['product_name'] for x in self.result]

    
interface = UserInterface()
data = OpenFoodData()

interface.showMenu()
answer = interface.getInputUser('menu')

if answer == 1:

            # show main categories
    interface.showData(data.get_categories())
    choice = interface.getInputUser('search')

            # show products related with choosen category
    interface.showData(data.get_one_category(choice))
    choice = interface.getInputUser('search')

            # show best equivalent products
    interface.showData(data.search_products(choice))
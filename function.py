#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlapi
import json

# show how many category in terminal
NUMBER_ITEMS_SHOWN = 20      


class UserInterface:

    """This class manage interaction with user."""

    def __init__(self):
        self.userChoice = ''

    def show_menu(self):
        print('1. Chercher un meilleur produit')
        print('2. Consulter les produits sauvegardés')

    def get_user_input(self, mode):     # need to upgrade

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

    def show_data(self, items):

        if len(items) > 1:
            for i, item in enumerate(items):
                print(i+1, item)
        else:
            print(items[0][0],items[0][1])


class OpenFoodData:

    """Manage all interaction with database. """

    def __init__(self):

        self.config = None
        with open('deployment/config.json', 'r') as file:
            self.config = json.load(file)

        self.sql = sqlapi.SqlApi(self.config['host'],
                                self.config['user'],
                                self.config['password'],
                                self.config['db'])
        self.result = ''


    def get_categories(self):
        req = self.sql.select('categories')
        self.result = self.sql.send_request(req)

        self.result = [x['category'] for x in self.result]
        return self.result

    def get_one_category(self, category_numero):

        category = str(category_numero)

        req = self.sql.select('category_product')
        req += self.sql.inner_join('products')
        req += self.sql.on('category_product.f_product', 'products.code')
        req += self.sql.where('f_category', category)

        self.result = self.sql.send_request(req)

        return [x['product_name'] for x in self.result]

        
    def search_products(self, choice):

        """Get specific catgory of searched product 
        then ask the db to find all product related of searched product
        """

        specific_category = self.result[choice-1]['specific_category']

        req = self.sql.select('products')
        req += self.sql.where('specific_category', specific_category)

        self.result = self.sql.send_request(req)
    
        #return [(x['product_name'], x['code']) for x in self.result]
        return [[self.result[0]['product_name'], self.result[0]['code']]]

    def get_product_link(self):
        return "https://fr.openfoodfacts.org/produit/{}/".format(self.result[0]['code'])

    def save_product(self):
        req = self.sql.insert('save_product', 'code_product')
        req += self.sql.values(self.result[0]['code'])

        self.sql.send_request(req)

    def get_save_product(self):
        req = self.sql.select('save_product')
        req += self.sql.inner_join('products')
        req += self.sql.on('save_product.code_product', 'products.code')
        self.result = self.sql.send_request(req)

        return [(x['product_name'], x['code']) for x in self.result]



interface = UserInterface()
data = OpenFoodData()

interface.show_menu()
answer = interface.get_user_input('menu')

# search mode
if answer == 1:

    # show main categories
    interface.show_data(data.get_categories())
    category_choice = interface.get_user_input('search')

    # show products related with choosen category
    interface.show_data(data.get_one_category(category_choice))
    product_choice = interface.get_user_input('search')

    # show product want to replace
    interface.show_data(data.search_products(product_choice))
    print(data.get_product_link())

    is_saved = input('Souhaitez vous sauvegarder le produit ?\n1 (oui), 0 (non) :\n') 
    if is_saved == '1':
        data.save_product()
        print('Produit sauvegardé avec succès')


# view mode
if answer == 2:
    interface.show_data(data.get_save_product())


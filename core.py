#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import deployment.sqlapi as sqlapi
import json

# show how many category in terminal
NUMBER_ITEMS_SHOWN = 20


class UserInterface:

    """This class manage interaction with user."""

    def __init__(self):
        self.userChoice = ''

    def show_menu(self):
        print('01. Chercher un meilleur produit')
        print('02. Consulter les produits sauvegardés')

    # need to upgrade
    def get_user_input(self, mode):

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

        if type(items[0]) == dict:
            items = [item['product_name'] for item in items]

        if len(items) > 1:
            for i, item in enumerate(items):
                print('{:02d}. {}'.format(i+1, item))

        # need to upgrade 
        else:
            item = items[0]
            [print(info) for info in item]


class OpenFoodData:

    """Manage all interaction with database. """

    def __init__(self):

        self.result = None
        self.config = None
        with open('deployment/config.json', 'r') as file:
            self.config = json.load(file)

        self.sql = sqlapi.SqlApi(self.config['host'],
                                self.config['user'],
                                self.config['password'],
                                self.config['db'])


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

        self.result = self.sql.send_request(req, NUMBER_ITEMS_SHOWN)

        return self.result

        
    def search_products(self, choice, main_category):

        """Get specific catgory of searched product 
        then ask the db to find all product related of searched product
        """

        specific_category = self.result[choice-1]['specific_category']

        req = self.sql.select('products')
        req += self.sql.where('specific_category', specific_category)

        self.result = self.sql.send_request(req)

        # first row it same product selected by user, so take the last row
        item = self.result[-1]

        # if not found equivalent product, search other product
        if len(self.result) == 1:

            # make a join to build request
            req = self.sql.select('category_product cp')
            req += self.sql.inner_join('products p')
            req += self.sql.on('cp.f_product', 'p.code')

            # search with main category
            req += self.sql.where('cp.f_category', str(main_category))

            # using words in product name to make search
            search_pattern = item['product_name'].split(' ')

            # pipe is OR operator
            search_pattern = '|'.join(search_pattern)
            req += " AND p.product_name REGEXP '{}'".format(search_pattern) # enhance
            
            item = self.sql.send_request(req)[-1]
        
        return [[item['product_name'],
                 item['code'],
                 item['brands'],
                 item['quantity'],
                 item['stores']]]

    def get_product_link(self):
        return "https://fr.openfoodfacts.org/produit/{}/".format(self.result[-1]['code'])

    def save_product(self):
        req = self.sql.insert('save_product', 'code_product')
        req += self.sql.values(self.result[-1]['code'])

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
    print(type(category_choice))

    # show products related with choosen category
    old_user_choice = data.get_one_category(category_choice)
    interface.show_data(old_user_choice)
    product_choice = interface.get_user_input('search')

    # show product want to replace
    old_product = old_user_choice[product_choice-1]
    old_code = old_product['code']
    print('Produit initial')
    print(old_product['product_name'], old_code, '\n')


    print('Produit trouvé')
    match_product = data.search_products(product_choice, category_choice)
    interface.show_data(match_product)
    print(data.get_product_link())

    print('01. Oui')
    print('02. Non')
    is_saved = input('Souhaitez vous sauvegarder le produit ? : ') 
    if is_saved == '1':
        data.save_product()
        print('Produit sauvegardé avec succès')


# view mode
if answer == 2:
    interface.show_data(data.get_save_product())


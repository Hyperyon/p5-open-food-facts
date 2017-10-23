#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlapi

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
        for i, item in enumerate(items):
            print(i+1, item)


class OpenFoodData:

    """Manage all interaction with database. """

    def __init__(self):
        self.sql = sqlapi.SqlApi('localhost', 'nico', 'password', 'OpenFoodFactsDb')
        self.result = ''

    def save_product(self, choice):
        req = self.sql.insert('save_product', 'code_product')
        req += self.sql.values(self.result[choice-1]['code'])

        self.sql.send_request(req)

    def search_products(self, choice):

        specific_category = self.result[choice-1]['specific_category']

        req = self.sql.select('products')
        req += self.sql.where('specific_category', specific_category)

        self.result = self.sql.send_request(req)
    
        return [(x['product_name'], x['code']) for x in self.result]

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

                
interface = UserInterface()
data = OpenFoodData()

interface.show_menu()
answer = interface.get_user_input('menu')

if answer == 1:

            # show main categories
    interface.show_data(data.get_categories())
    category_choice = interface.get_user_input('search')

            # show products related with choosen category
    interface.show_data(data.get_one_category(category_choice))
    product_choice = interface.get_user_input('search')

            # show best equivalent products
    interface.show_data(data.search_products(product_choice))
    better_choice = interface.get_user_input('search')

    data.save_product(better_choice)
# -*- coding:Utf-8 -*-
import urllib.request as get
import json


class UserInterface:

    """This class manage interaction with user."""

    def __init__(self):
        self.userChoice = ''

    def showMenu(self):
        print('1. Chercher un meilleur produit')
        print('2. Consulter les produits sauvegardés')

    def getInputUser(self):
        while 'is not numeric choice':
            self.userChoice = input('\nVotre choix : ')

            if not self.userChoice.isnumeric():
                print('Saisie erronee')
            elif not self.checkInput():
                print('Ce choix n\'existe pas')
            else:
                break
        if self.userChoice == '1':
            self.userChoice = input('Saisir un produit : ')
            return self.userChoice
        else:
            return False

    def checkInput(self):
        if self.userChoice in ('1', '2'):
            return True
        else:
            return False



class OpenFoodApi:

    """Manage all interaction with Open food facts API."""


    url_part1 = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms='
    url_part2 = '&search_simple=1&action=process&json=1'
    req = 'pepito'

    def getData(self):
        data = get.urlopen(self.req).read()
        data = data.decode('Utf-8')     # we receive byte data
        data = json.loads(data)

        nb_item = data['count']

        if nb_item:     # at least 1 item found

            if nb_item > 20:    # avoid range index error
                nb_item = 20

            for index in range(nb_item):
                print(str(index+1) + '. ' + data['products'][index]['product_name'])


    def genRequest(self, request):
        # need to check if alphanumeric value
        self.req = self.url_part1+request+self.url_part2
        self.getData()


z = UserInterface()

z.showMenu()
answer = z.getInputUser()

if answer:
    a = OpenFoodApi()
    a.genRequest(answer)



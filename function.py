#!/usr/bin/env python3
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



class OpenFoodData:

    """Manage all interaction with database"""
    def __init__(self):
        pass

z = UserInterface()

z.showMenu()
answer = z.getInputUser()

if answer:
    print(answer)



![python](https://img.shields.io/badge/python-3.5-blue.svg)

P5 - Open food facts
===
Program allow to search better food with information based on Open Food Facts


class UserInterface
---

Class show menu and user interface 

    show_menu(self)

Show main menu like below
```
01. Chercher un meilleur produit
02. Consulter les produits sauvegardés
```

    get_user_input(self, mode) -> return int(userChoice)

Check user input in terminal

    show_data(self, items)

Show data like catoegories or list of products



class OpenFoodData
---

Manage intput and output data in database

    save_product(self, request)

Saving product which selected by user

    search_products(self, choice)

Search equivalent products


    get_categories(self) -> return list

Get in database a list of available categories


    get_one_category(self, choice) -> return list

Get family of product selected by user


    get_save_product(self) -> return list

Get all saved products saved before by user


class SqlApi
---

This class manage all SQL request sent by `OpenFoodData` class

    send_request(req, self)

Excute the request

    add_quotes(self, element, *doublequotes):

Adding quote to generate request (usefull on values)

    add_brackets(self, element):
Adding brackets on element request syntax

    select(self, table):
Generate first step of request syntax

    where(self, table, value):
Generate where sql request syntax

    insert(self, table, *field):
Generate insert sql request syntax

    values(self, val):
Generate values request syntax
 
    inner_join(self, table):
Generate inner join request syntax

    on(self, field, field_2):
Generate 'on' request syntax

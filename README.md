
```python
class UserInterface
```

Cette classe va gérer l'affichage du menu et des données et les saisies de l'utilisateur

    show_menu(self)

Affiche le menu principal qui propose soit 
1. la recherche d'un produit
2. l'affichage des produits enrregistrés


    get_user_input(self, mode) -> return int(userChoice)

Gère et vérifie ce que l'utilisateur saisie dans le terminal

    show_data(self, items)

Affiche les données telles que les catégorie ou les produits d'une catégorie spécifique



```python
class OpenFoodData
```

La classe s'occupe de récupérer et d'insérer des informations dans la base de données


    save_product(self, request)

Méthode pour sauvegarder un produit en base de données

    search_products(self, choice)

Effectuer une recherche pour trouver un produit équivalent


    get_categories(self) -> return list

Obtenir les catégories de produits


    get_one_category(self, choice) -> return list

Obtenir les produits d'une catégorie particulière


    get_save_product(self) -> return list

Obtenir les produits choisis précédemment par l'utilisateur


```python
class SqlApi
```

Cette classe gère les requêtes SQL en se chargeant de formater correctement les demandes envoyées par la classe `OpenFoodData`

    send_request(self)

Exécute la requête

    add_quotes(self, element, *doublequotes):

Rajoute des quotes là où c'est nécessaire (utile particule sur les valeurs)

    add_brackets(self, element):
Ajoute des parenthèses

    select(self, table):
Génère une prérequête pour la requête sql SELECT

    where(self, table, value):
Génère une prérequête pour la requête sql WHERE

    insert(self, table, *field):
Génère une prérequête pour la requête INSERT

    values(self, val):
Génère une prérequête pour la requête VALUES

    inner_join(self, table):
Génère une prérequête pour la requête INNER JOIN

    on(self, field, field_2):
Génère une prérequête pour la requête ON

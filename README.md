
```python
class UserInterface
```

Cette classe va gérer l'affichage du menu et des données et les saisies de l'utilisateur

> showMenu(self)

Affiche le menu principal qui propose soit 
1. la recherche d'un produit
2. l'affichage des produits enrregistrés


> getInputUser(self, mode) -> return int(userChoice)

Gère et vérifie ce que l'utilisateur saisie dans le terminal

> showData(self, items)

Affiche les données telles que les catégorie ou les produits d'une catégorie spécifique



```python
class OpenFoodData
```

La classe s'occupe de récupérer et d'insérer des informations dans la base de données


> save_product(self, request)

Méthode pour sauvegarder un produit en base de données

> search_products(self, choice)

Effectuer une recherche pour trouver un produit équivalent


> get_categories(self) -> return list

Obtenir les catégories de produits


> get_one_category(self, choice) -> return list

Obtenir les produits d'une catégorie particulière

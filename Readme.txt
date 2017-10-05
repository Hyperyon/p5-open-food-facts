Au démarrage, le script propose à l'utilisateur deux choix
1 - Quel aliment souhaitez-vous remplacer ?
2 - Retrouver mes aliments substitués.

Tant que utilisateur n'a pas tapé un chiffre, il affichera ce menu
-- vérification de l'user input pour savoir si c'est bien une valeur numérique qui a été saisie


L'utilisateur tape sa recherche
-- vérif que l'user input, le nom du produit doit être de type alphanumérique (voire que la possibilité de faire recherche qu'avec des lettres)


Le programme génère la requête à l'API Open food fact
-- vérif que l'API nous retourne une réponse, si une erreur s'affiche pouvoir le signaler que sa recherche ne peut aboutir ?


Le programme traite les données d'API
La fonction fait le tri dans les informations reçues, il n'affiche dans le terminal que les informations pertinentes

Le programme affiche les données dans le terminal
Un formatage particulier sera peut-être utile

L'utilisateur sélectionne le produit qui le convient en tapant la valeur correspondant au produit équivalent
--pareil vérif que le choix est bien un integer

Le programme génère la requête SQL

Le programme exécute la requête pour effectuer la sauvegarde en base de données mySQL

L'utilisateur décide de retrouver ses aliments substitués
Le script va effectuer une requête type Select dans la bdd

Le programme va finalement afficher les données récupérées préalablement en formation si nécessaire les informations.

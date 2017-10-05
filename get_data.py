# -*- coding:Utf-8 -*-
import json
import urllib2 as get


url = 'https://fr.openfoodfacts.org/cgi/search.pl?search_terms=delacre&search_simple=1&action=process&json=1'


data = json.load(get.urlopen(url))

nb_item = data['count']

if nb_item:     # at least 1 item found

    if nb_item > 20:    # avoid range index error
        nb_item = 20

            # code works
    #for index in xrange(nb_item):
    #    print data['products'][index]['product_name']

    #id = data['products'][0]['id']
    lang, category = data['products'][0]['categories_tags'][-1].split(':')
    print(category)
    print(lang)

    url = "https://fr.openfoodfacts.org/categorie/"+category+"&json=1"

    if lang == 'en':       # sometimes we get english category, but we need fr version
        fr_category = get.urlopen(url).read().split('fr:')[1]
        fr_category = fr_category.split('"/>')[0]
        print(fr_category)
        category = fr_category


    url = "https://fr.openfoodfacts.org/categorie/"+category+"&json=1"
    data2 = json.load(get.urlopen(url))
    nb_item2 = data2['count']

    if nb_item2 > 20:
        nb_item2 = 20

    for index in xrange(nb_item2):
        print data2['products'][index]['product_name']

else:
    print('Aucun produit trouvé')




"""





data = json.load(get.urlopen(url))

for element in data['products']:
    print element['product_name']"""
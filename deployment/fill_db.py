#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request as get
import time as t
import sqlapi


# this var define nb categories we get
MAX_NB_CATEGORY = 20
cat_url = 'https://fr.openfoodfacts.org/categories.json'
#product_url = 'https://fr.openfoodfacts.org/categorie/'


config = None

with open('config.json', 'r') as file:
    config = json.load(file)

# Remove after
config['db'] = 'oui'

# connect to database
sql = sqlapi.SqlApi(config['host'],
                    config['user'],
                    config['password'],
                    config['db'])



def get_data(full_url):
    data = get.urlopen(full_url).read()
    data = data.decode('Utf-8')     # we receive byte data
    json_data = False

    try:
        json_data = json.loads(data) 
    except json.decoder.JSONDecodeError :
        print('failed request')
    finally:
        return json_data


def get_category():
    data = None

    with open('category.json', 'r+') as file:
        content_file = file.read()
        if content_file:
            print('Data already exist')
            data = json.loads(content_file)
        else:
            data = get_data(cat_url)
            json.dump(data, file)

    return data

def fill_product_table(data):
    field = ['code', 'product_name', 'quantity', 'brands', 'stores', 'specific_category']
    for item in data['products']:
        print(item['product_name'], item['code'])
        #req = sql.insert('products', )

data = get_category()


'''# insert categories into database
for category in data['tags'][:MAX_NB_CATEGORY]:
    request = sql.insert('categories', 'category')
    request += sql.values(category['name'])
    sql.send_request(request)'''


for index in range(MAX_NB_CATEGORY):
    current_cat = data['tags'][index]['name']
    print('\nGet item from ' + current_cat,)

    for page in range(1, 2):
        url = data['tags'][index]['url'] + '&json='+str(page)
        fill_product_table(get_data(url))
        
        # avoid to overload server
        t.sleep(3)

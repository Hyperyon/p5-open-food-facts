#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request as get
import time as t
import sqlapi


# this var define nb categories we get
MAX_NB_CATEGORY = 2

# define how many product we want : 20 products / page
MAX_NB_PAGE = 2

cat_url = 'https://fr.openfoodfacts.org/categories.json'
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
    # we receive byte data
    data = data.decode('Utf-8')
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


def no_empty_str(x):
    if len(x) == 0:
        x = 'aucun'
    return x

def fill_product_table(data, main_category):
    wanted_keys = ['product_name','quantity','brands', 'stores_tags','code']

    for item in data['products']:

        json_item_keys = list(item.keys())

        # sometimes product missing some wanted information
        if len(set(json_item_keys) & set(wanted_keys)) != 5:
            print('Missing field for "{}" product'.format(item['product_name']))
            # if yes, we don't execute instructions below
            continue

        # get last category
        specific_category = item['categories'].split(',')[-1]
        # remove start and end space from str
        specific_category = specific_category.strip()

        values = [item['code'], item['product_name'],
                  item['quantity'], item['brands'],
                  item['stores'], specific_category]

        # each time we have empty value in field, we replace by 'aucun'
        values = list(map(no_empty_str, values))

        # part 1/2 : generate INSERT INTO request
        req = sql.insert('products',
                         'code',
                         'product_name',
                         'quantity',
                         'brands',
                         'stores',
                         'specific_category')

        # part 2/2 : generate VALUES request
        req += sql.values(values)

        # finally excecute sql request
        sql.send_request(req)
        print(item['product_name'])

        fill_cat_product_table(main_category, item['code'])

def fill_cat_product_table(category, product_code):
    req = sql.insert('category_product', 'f_category', 'f_product')
    req += sql.values([category, product_code])
    sql.send_request(req)


def fill_category_table():

    # get nb of categories in db if exist
    result = sql.send_request('SELECT COUNT(`category`) FROM categories ')
    nb_categories = result[0]['COUNT(`category`)']

    # check to avoid duplicate category
    if (nb_categories < MAX_NB_CATEGORY):
        # insert categories into database
        for category in data['tags'][:MAX_NB_CATEGORY]:
            request = sql.insert('categories', 'category')
            request += sql.values(category['name'])
            sql.send_request(request)
    else:
        print('Categories table already filled')


def remove_duplicate_row():
    req = '''SET FOREIGN_KEY_CHECKS = 0;
             DELETE t1 FROM products t1
             INNER JOIN products t2
             WHERE t1.id < t2.id and t1.code = t2.code;
             SET FOREIGN_KEY_CHECKS = 1;'''

    sql.send_request(req)


data = get_category()


fill_category_table()


for index in range(MAX_NB_CATEGORY):
    current_cat = data['tags'][index]['name']
    print('\nGet item from ' + current_cat,)

    for page in range(1, MAX_NB_PAGE+1):
        url = data['tags'][index]['url'] + '&json='+str(page)

        # take index to determine category
        fill_product_table(get_data(url), str(index+1))
        
        # avoid to overload server
        t.sleep(3)

remove_duplicate_row()

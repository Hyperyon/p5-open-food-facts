#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import urllib.request as get
import time as t


MAX_CATEGORY = 2
cat_url = 'https://fr.openfoodfacts.org/categories.json'
#product_url = 'https://fr.openfoodfacts.org/categorie/'
# get category first

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

    '''for index in range(MAX_CATEGORY):
                    categories.append(data['tags'][index]['name'])'''
    return data

def filtered_data(data):
    for item in data['products']:
        print(item['product_name'])


data = get_category()


for index in range(MAX_CATEGORY):
    print('\nGet item from '+data['tags'][index]['name'],)

    for page in range(1, 2):
        url = data['tags'][index]['url'] + '&json='+str(page)
        filtered_data(get_data(url))

        t.sleep(3)

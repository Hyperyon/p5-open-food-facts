#!/usr/bin/env python3
# -*- coding:Utf-8 -*-

import json
import urllib.request as get
import pickle as pick
import time as t


url = 'https://fr.openfoodfacts.org/categorie/'
link  = 'https://fr.openfoodfacts.org/produit/'
category = ''


with open('categorie.txt', 'r') as f:
    category = f.read().split('\n')

def save_data(data):
    with open('filter_data5', 'wb') as data_file:
        p = pick.Pickler(data_file)
        p.dump(data)



def no_empty(x):
    if len(x) == 0:
        x = 'aucun'
    return x


def get_data(full_url):
    data = get.urlopen(full_url).read()
    data = data.decode('Utf-8')     # we receive byte data
    state = False

    try:
        state = json.loads(data) 
    except json.decoder.JSONDecodeError :
        print('failed request')
    finally:
        return state

def gen_filter_data(data, main_category):
    max_count = 20
    data_sorted = []

    for index in range(max_count):
        item = data['products'][index]['product_name']

        json_answer_keys = list(data['products'][index].keys())
        wanted_keys = ['product_name','quantity','brands', 'stores_tags','code']

        if item and len(set(json_answer_keys) & set(wanted_keys)) == 5:        # avoid empty item
            a = data['products'][index]['categories'].split(',')
            group_product = [main_category, a[-1]] #       get generic & specific category

            #print(data['products'][index]['ingredients_tags'])
            temp = [data['products'][index]['product_name'],
                    data['products'][index]['quantity'],
                    data['products'][index]['brands'],
                    data['products'][index]['stores_tags'],
                    data['products'][index]['code'],
                    group_product,]

            temp = list(map(no_empty, temp))
            print(temp[0])

            data_sorted.append(temp)

    return data_sorted



def check_data():
    with open('filter_data5', 'rb') as f:
        data = pick.Unpickler(f)
        return data.load()

sorted_data = []

for page in range(20, 25):
    for cat in category[:100]:      # get only 100 first categories
        req = url + cat + '/'+ str(page) +'.json'
        print('\n\n'+req)

        data = get_data(req)

        if data: #if data not empty
                    # this-my-category, so I convert '-' to space
            data = gen_filter_data(data, cat.replace('-', ' '))
            sorted_data += data

        t.sleep(3)

save_data(sorted_data)


"""a = check_data()
[print(x) for x in a[:35]]
print(len(a))"""


import pymysql
import pymysql.cursors
import pickle as pick


'''connexion = pymysql.connect(host='localhost',user='nico',password='password',
    db='OpenFoodFactsDb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)


sql = connexion.cursor()

req = "INSERT INTO `categories` (`numero`, `category`) VALUES (NULL, 'pate'), (NULL, 'jambon');"
sql.execute(req)

connexion.commit()
'''

def send_data(request):
    connexion = pymysql.connect(host='localhost',user='nico',password='password',
    db='OpenFoodFactsDb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

    sql = connexion.cursor()
    sql.execute(request)
    connexion.commit()


def get_data(): #filter_data4 NOK
    with open('filter_data5', 'rb') as f:
        data = pick.Unpickler(f)
        return data.load()


data = get_data()




def join_data(data):
    if type(data) is list:
        data = ' '.join(data)
    return data


def add_quotes(data): # for sql resquest
    return '"' + data + '"'

for index, item in enumerate(data):

       # merge each field with 2 ou more elements except last field (categories)
    data[index] = list(map(join_data, item[:-1]))
        # adding main and specific categories
    data[index] += item[-1]
    data[index] = list(map(add_quotes, data[index]))

    data[index] = '(' + ','.join(data[index]) + ')'


data = ', '.join(data)






start_req = """INSERT INTO `products` (`product_name`, `quantity`, `brands`, `stores`, `code`, `main_category`, `specific_category`) """
req = start_req + "VALUES " +  data + ";"

#send_data(req)




'''
 ('kamembert', '50', 'delaballe', 'magasin', '007', 'cereales en grains', 'special k')

'''




'''
        # Generate category in db

for item in data:
    main_category = item[-1][0]
    if not main_category in categories :
        categories.append(main_category)

payload_req = ""

for category in categories:
    payload_req += "(NULL, '" + category + "'), "

start_req = """INSERT INTO `categories` (`numero`, `category`) VALUES """
req = start_req + payload_req[:-2] + ";"



'''


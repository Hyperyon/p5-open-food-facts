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


def get_data():
    with open('filter_data', 'rb') as f:
        data = pick.Unpickler(f)
        return data.load()


data = get_data()

        #effectuer un map ''.join(x) avant de mettre en bdd
[print(x[:-1]) for x in data[:20]]

'''
for item in data:
    main_category = item[-1][0]
    if not main_category in categories :
        categories.append(main_category)

payload_req = ""

for category in categories:
    payload_req += "(NULL, '" + category + "'), "

start_req = """INSERT INTO `categories` (`numero`, `category`) VALUES """
req = start_req + payload_req[:-2] + ";"'''



'''INSERT INTO `products` (`product_name`, `quantity`, `brands`, `stores`, `code`, `main_category`, `specific_category`) 
VALUES ('kamembert', '50', 'delaballe', 'magasin', '007', 'cereales en grains', 'special k')'''





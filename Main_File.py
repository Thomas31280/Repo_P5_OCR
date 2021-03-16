import mysql.connector as SQLcmd
import requests

import data_checking

"""
Data recovery from the API.
"""
requestpost_products = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=500&page=1&json=true&fields=product_name,nutriscore_grade,url,pnns_groups_1,categories,generic_name")
print(requestpost_products) #Check the response of API ( ok if 200 )
response_data_products = requestpost_products.json()

requestpost_categories = requests.get("https://fr.openfoodfacts.org/categories.json")
print(requestpost_categories)
response_data_categories = requestpost_categories.json()

"""
Generating a database from the JSON data.
"""
# Connexion to MySQL :
cnx = SQLcmd.connect(user='root', password='edgard31280', host='localhost')
cursor = cnx.cursor()

# Database creation
DB_NAME = "db_project_5"

cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))
cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
print("Database {} created successfully.".format(DB_NAME))
cnx.database = DB_NAME

# Table creation with connector :
TB1_NAME = "product"
TB2_NAME = "hystory"
TB3_NAME = "categories"

cursor.execute(
    "CREATE TABLE `{}` ("
    "  `id_product` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `url` TEXT,"
    "  `product_group` VARCHAR(60),"
    "  `nutriscore` CHAR(1),"
    "  `categories` TEXT,"
    "  `product_name` VARCHAR(60),"
    "  `generic_name` VARCHAR(70),"
    "  PRIMARY KEY (`id_product`)"
    ") ENGINE=InnoDB".format(TB1_NAME))
print("Table {} created successfully.".format(TB1_NAME))

cursor.execute(
    "CREATE TABLE `{}` ("
    "  `id_category` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `category_name` VARCHAR(70),"
    "  PRIMARY KEY (`id_category`)"
    ") ENGINE=InnoDB".format(TB3_NAME))
print("Table {} created successfully.".format(TB3_NAME))

# Upload data from OpenFoodFact into table table_produits:

#number_of_fields_TB1 = cursor.execute("SELECT count (*) FROM information_schema.columns WHERE table_name='product'")

for category in response_data_categories["tags"]:
    print(category['name'])
    cmd = "INSERT INTO categories VALUES (%s)"
    data_to_insert = (category['name'])
    cursor.execute(cmd,data_to_insert)
    cnx.commit()

for product in response_data_products["products"]:

    #Appeler méthode de vérification de l'existence des éléments dans le dictionnaire
    #C'est le product traité par la méthode ci-dessus qui sera injecté dans la data
    Check_data = data_checking.data_checking(product, number_of_fields_TB1)
    if Check_data:
        sql = "INSERT INTO product (url,product_group,nutriscore,categories,product_name,generic_name) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (product['url'],product['pnns_groups_1'],product['nutriscore_grade'],product['categories'],product['product_name'],product['generic_name'])
        cursor.execute(sql,data)
        cnx.commit()
    else:
        pass
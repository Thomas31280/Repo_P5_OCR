import mysql.connector as SQLcmd
import requests

"""
Data recovery from the API.
"""
requestpost = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=500&page=1&json=true&fields=product_name,nutriscore_grade,url,pnns_groups_1,categories,generic_name")
print(requestpost) #Check the response of API ( ok if 200 )
response_data = requestpost.json()

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
TB1_NAME = "table_produits"
TB2_NAME = "table_historique"

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

# Upload data from OpenFoodFact into table table_produits:
for product in response_data["products"]:
    cursor.execute("INSERT INTO {}""(id_product)""VALUES (NULL)".format(TB1_NAME))
    for field in product:
        if field in ("categories", "generic_name", "product_name", "url") :
            cursor.execute("INSERT INTO {}""({})""VALUES ({})".format(TB1_NAME, field, product[field]))
        elif field == "pnns_group_1":
            cursor.execute("INSERT INTO {}""({})""VALUES ({})".format(TB1_NAME, "product_group", product[field]))
        elif field == "nutriscore_grade":
            cursor.execute("INSERT INTO {}""({})""VALUES ({})".format(TB1_NAME, "nutriscore", product[field]))

print(cursor.execute("SELECT * FROM table_produits"))
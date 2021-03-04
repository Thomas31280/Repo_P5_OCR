import mysql.connector as SQLcmd
import requests

"""
Data recovery from the API.
"""
test_var = requests.get("https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=500&page=1&json=true&fields=product_name,nutriscore_grade,url,stores,pnns_groups_1,categories,generic_name")
print(test_var) #Check the response of API ( ok if 200 )

"""
Generating a database from the JSON data.
"""
# Connexion to MySQL :
cnx = SQLcmd.connect(user='root', password='edgard31280', host='localhost')
cursor = cnx.cursor()

# Database creation
DB_NAME = "db_test"

cursor.execute("DROP DATABASE IF EXISTS {}".format(DB_NAME))
cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
print("Database {} created successfully.".format(DB_NAME))
cnx.database = DB_NAME

# First test on database (table creation) with connector :
TB_NAME = "table_test"

cursor.execute(
    "CREATE TABLE `table_test` ("
    "  `id` SMALLINT NOT NULL AUTO_INCREMENT,"
    "  `Field_1` date NOT NULL,"
    "  `Field_2` varchar(14) NOT NULL,"
    "  `Field_3` varchar(16) NOT NULL,"
    "  `Field_4` enum('M','F') NOT NULL,"
    "  `Field_5` date NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")
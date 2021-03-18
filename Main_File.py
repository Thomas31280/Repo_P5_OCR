import mysql.connector as SQLcmd

from Class import data_checking
from Class import http_requests
from Class import database_administration
from Class import constant_storage

"""
Data recovery from the API.
"""
response_data_products = http_requests.Requests("https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size=500&page=1&json=true&fields=product_name,nutriscore_grade,url,pnns_groups_1,categories,generic_name")

"""
Generating a database from the JSON data.
"""
# Connexion to MySQL :
cnx = database_administration.Database.connexion_to_mysql()
cursor = cnx.cursor()

# Database creation / selection

database_administration.Database.database_creation(constant_storage.DB_NAME, cursor, cnx)
database_administration.Database.database_selection(cursor, constant_storage.DB_NAME)

# Table creation with connector :
database_administration.Database.table_creation(cursor, cnx)

# Upload data from OpenFoodFact into table table_produits:

database_administration.Database.load_products_in_table(response_data_products, cnx, cursor)
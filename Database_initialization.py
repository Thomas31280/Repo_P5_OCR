import mysql.connector as SQLcmd

from Class import http_requests
from Class import database_administration
import constant_storage

"""
Data recovery from the API.
"""


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

database_administration.Database.load_categories_in_table(cnx, cursor)
database_administration.Database.load_products_in_table(cnx, cursor)
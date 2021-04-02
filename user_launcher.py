from Class import database_administration
from Class import user
import constant_storage

cnx = database_administration.Database.connexion_to_mysql()
cursor = cnx.cursor()

database_administration.Database.database_selection(cursor, constant_storage.DB_NAME)
user = user.User()
user.user_main_page(cursor, cnx)

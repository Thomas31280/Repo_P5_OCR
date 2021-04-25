from Class import database_administration
import constant_storage


cnx = database_administration.Database.connexion_to_mysql()
cursor = cnx.cursor()

database_administration.Database.database_creation(constant_storage.DB_NAME,
                                                   cursor, cnx)
database_administration.Database.database_selection(cursor,
                                                    constant_storage.DB_NAME)

database_administration.Database.table_creation(cursor, cnx)

database_administration.Database.load_categories_in_table(cnx, cursor)
database_administration.Database.load_products_in_table(cnx, cursor)

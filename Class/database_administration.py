import mysql.connector as SQLcmd
from mysql.connector import errorcode

from . import constant_storage
from . import tables
from . import data_checking

class Database:

    @classmethod
    def connexion_to_mysql(cls):

        cnx = SQLcmd.connect(user=constant_storage.USER, password=constant_storage.PASSWORD, host=constant_storage.HOST)
        return cnx


    @classmethod
    def database_creation(cls, db_name, cursor, connexion):

        cursor.execute("DROP DATABASE IF EXISTS {}".format(db_name))
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
        print("Database {} created successfully.".format(db_name))
        connexion.database = db_name
    

    @classmethod
    def database_selection(cls, cursor, db_name):
        
        try:
            cursor.execute("USE {}".format(db_name))
        except SQLcmd.Error:
            print("Database {} does not exists.".format(db_name))

    
    @classmethod
    def table_creation(cls, cursor, connexion):

        for table_name in tables.TABLES:
            table_description = tables.TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except SQLcmd.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        
        connexion.commit()
    
    @classmethod
    def load_products_in_table(cls, data_json, connexion, cursor):

        for product in data_json["products"]:

            Check_data = data_checking.data_checking(product, 7)
            if Check_data:
                sql = "INSERT INTO product (url,product_group,nutriscore,categories,product_name,generic_name) VALUES (%s, %s, %s, %s, %s, %s)"
                data = (product['url'],product['pnns_groups_1'],product['nutriscore_grade'],product['categories'],product['product_name'],product['generic_name'])
                cursor.execute(sql, data)
                connexion.commit()
            else:
                pass
    
    @classmethod
    def load_categories_in_table(cls, connexion, cursor):

        with open("categories.txt") as cat:
            for line in cat:
                sql = "INSERT INTO categories (category_name) VALUES (%s)"
                data = (line, )
                cursor.execute(sql, data)
                connexion.commit()
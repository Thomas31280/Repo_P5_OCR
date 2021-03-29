import mysql.connector as SQLcmd

import constant_storage

class User:

    def __init__(self):
        
        self.first_try = True


    def user_main_page (self, cursor):
        
        if self.first_try :
            user_answer = input("Veuillez choisir une catégorie en entrant le chiffre correspondant, puis appuyez sur entrée. Sinon, appuyez sur Q pout quitter le programme : ")
        else :
            user_answer = input("Vous pouvez sélectionner une autre catégorie, ou quitter le programme avec Q : ")
        
        if user_answer == "Q":
            print("Merci, et à bientôt")

        elif user_answer in (range(1, len(constant_storage.CATEGORIES + 1))):
            self.products_by_category(user_answer, cursor)
        
        else:
            print("Entrée non valide.")
            self.user_main_page(cursor)
    

    def products_by_category (self, user_answer, cursor):

        query = ("SELECT id_product, product_name FROM product INNER JOIN category ON product.categories = category.category_name WHERE product.categories = %s")
        answer = (user_answer, )
        cursor.execute(query, answer)
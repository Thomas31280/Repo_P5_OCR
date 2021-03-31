import mysql.connector as SQLcmd

import constant_storage

class User:

    def __init__(self):
        
        self.first_try = True


    def user_main_page (self, cursor):
        
        user_answer = input("Tapez 1 si vous souhaitez remplacer un aliment, 2 si vous souhaitez retrouver vos aliments substitués. Sinon, tapez Q pour quitter le programme : ")
        
        if user_answer == "Q":
            print("Merci, et à bientôt")

        elif user_answer == "1":
            
            cursor.execute("SELECT * FROM category ORDER BY id_category")
            myresult = cursor.fetchall()
            
            for category in myresult:
                print(category)
            
            user_choice = input("Veuillez choisir une catégorie en entrant le chiffre correspondant, puis appuyez sur entrée : ")

            if int(user_choice) in range(1, len(constant_storage.CATEGORIES )+1):
                self.products_by_category(user_choice, cursor)
            
            else:
                print("Entrée non valide.")
                self.user_main_page(cursor)

        elif user_answer == "2":
            pass
        
        else:
            print("Entrée non valide.")
            self.user_main_page(cursor)
    

    def products_by_category (self, user_choice, cursor):
        
        id_products_returned = []
        
        query = ("SELECT id_product, product_name FROM product INNER JOIN category ON product.categories = category.category_name WHERE category.id_category = %s")
        answer = (int(user_choice), )
        cursor.execute(query, answer)
        myresult = cursor.fetchall()

        for product in myresult:
            id_products_returned.append(product[0])
            print(product)
        
        user_choice_2 = input("Veuillez choisir un produit parmi ceux proposés, en entrant son numéro. Sinon, quittez le programme avec Q : ")

        if int(user_choice_2) in id_products_returned:
            query = ("SELECT nutriscore FROM product WHERE product.id_product = %s")
            answer = (int(user_choice_2), )
            cursor.execute(query, answer)
            myresult = cursor.fetchall()
            
            for result in myresult:
                nutriscore_product = result[0]
            
            self.substitute_proposal(user_choice, nutriscore_product, cursor)

        elif user_choice_2 == "Q":
            print("Merci, et à bientôt")  ###PROBLEM TO SOLVE HERE###
            
        
        else:
            print("Entrée non valide.")
            self.products_by_category(user_choice, cursor)
        
    
    def substitute_proposal (self, user_choice, nutriscore_product, cursor):

        id_products_returned = []
        

        query = ("SELECT id_product, product_name, stores, url FROM product INNER JOIN category ON product.categories = category.category_name WHERE category.id_category = %s AND product.nutriscore = %s")
        answer = (int(user_choice), nutriscore_product)
        cursor.execute(query, answer)
        myresult = cursor.fetchall()

        for product in myresult:
            id_products_returned.append(product[0])
            print(product)
import mysql.connector as SQLcmd

import constant_storage

class User:

    def __init__(self):
        
        self.first_try = True


    def user_main_page (self, cursor, connexion):
        
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
                self.products_by_category(user_choice, cursor, connexion)
            
            else:
                print("Entrée non valide.")
                self.user_main_page(cursor, connexion)

        elif user_answer == "2":
            
            query = ("SELECT * FROM favorites")
            cursor.execute(query)
            myresult = cursor.fetchall()
            
            for result in myresult:
                print(result)
            
            legit_request = False

            while legit_request == False:
                user_choice_5 = input("Si vous souhaitez poursuivre, tapez 1, sinon, tapez Q pour quitter le programme : ")

                if user_choice_5 == "Q":
                    print("Merci, et à bientôt")
                
                elif user_choice_5 == "1":
                    self.user_main_page(cursor, connexion)
                
                else:
                    print("Entrée non valide")
        
        else:
            print("Entrée non valide.")
            self.user_main_page(cursor, connexion)
    

    def products_by_category (self, user_choice, cursor, connexion):
        
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
            
            self.substitute_proposal(user_choice, nutriscore_product, cursor, connexion)

        elif user_choice_2 == "Q":
            print("Merci, et à bientôt")  ###PROBLEM TO SOLVE HERE###
            
        
        else:
            print("Entrée non valide.")
            self.products_by_category(user_choice, cursor, connexion)
        
    
    def substitute_proposal (self, user_choice, nutriscore_product, cursor, connexion):

        id_products_returned = []
        

        ###PROBLEM TO SOLVE HERE###

        if nutriscore_product == None:
            print("Le produit que vous avez sélectionné ne possède pas d'information liée à son nutriscore. Par défaut, nous vous proposons les produits de sa catégorie pour lesquels aucune information de nutriscore existe :")
            query = ("SELECT id_product, product_name, stores, url FROM product INNER JOIN category ON product.categories = category.category_name WHERE category.id_category = %s AND product.nutriscore = NULL")
            answer = (int(user_choice), )

        else:
            answer = (int(user_choice), nutriscore_product)
            query = ("SELECT id_product, product_name, stores, url FROM product INNER JOIN category ON product.categories = category.category_name WHERE category.id_category = %s AND product.nutriscore = %s")

        cursor.execute(query, answer)
        myresult = cursor.fetchall()
        
        for product in myresult:
            id_products_returned.append(product[0])
            print(product)
        
        user_choice_3 = input("Si vous souhaitez ajouter un produit à vos favoris, veuillez choisir entrer son numéro. Sinon, appruyez sur Q pour quitter le programme : ")

        if int(user_choice_3) in id_products_returned:
            self.add_product_in_favorites(user_choice_3, cursor, connexion)

        elif user_choice_3 == "Q":
            print("Merci, et à bientôt")
        
        else:
            print("Entrée non valide")
            self.substitute_proposal(user_choice, nutriscore_product, cursor, connexion)
        
    
    def add_product_in_favorites (self, product_id, cursor, connexion):
        
        neutral_cursor = cursor
        legit_request = False
        
        query = ("INSERT INTO favorites (id_product,url,categories,product_name,nutriscore,stores) SELECT id_product,url,categories,product_name,nutriscore,stores FROM product WHERE product.id_product = %s")
        id_product = (int(product_id), )
        cursor.execute(query, id_product)
        connexion.commit()

        while legit_request == False:
            user_choice_4 = input("Si vous souhaitez poursuivre, tapez 1, sinon, tapez Q pour quitter le programme : ")
            if int(user_choice_4) == 1:
                self.user_main_page(neutral_cursor, connexion)
                legit_request = True
            
            elif user_choice_4 == "Q":                   ###PROBLEM TO SOLVE HERE###
                print("Merci, et à bientôt")
                legit_request = True
            
            else:
                print("Entrée non valide")
            
import mysql.connector as SQLcmd
import os

import constant_storage

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

class User:

    def __init__(self):
        pass

    def user_main_page (self, cursor, connexion):

        clear()
        user_answer = input("1 - Quel aliment souhaitez-vous remplacer ?\n2 - Retrouver mes aliments substitués.\nQ - Quitter le programme\n")
        
        if user_answer == "Q":
            print("Merci, et à bientôt")

        elif user_answer == "1":
            
            clear()
            cursor.execute("SELECT * FROM category ORDER BY id_category")
            myresult = cursor.fetchall()
            
            for category in myresult:
                print(category)
            
            user_choice = input("\nVeuillez choisir une catégorie en entrant le chiffre correspondant, puis appuyez sur entrée : ")

            if user_choice.isdigit():
                if int(user_choice) in range(1, len(constant_storage.CATEGORIES )+1):
                    self.products_by_category(user_choice, cursor, connexion)
            
            else:
                print("Entrée non valide.")
                self.user_main_page(cursor, connexion)

        elif user_answer == "2":
            
            clear()
            print("Voici la liste de vos produits sauvegardés :\n")
            query = ("SELECT product_name, nutriscore, url, stores FROM product INNER JOIN favorite ON product.id_product = favorite.id_product")
            cursor.execute(query)
            myresult = cursor.fetchall()
            
            for result in myresult:
                print(result)
            
            legit_request = False

            while legit_request == False:
                user_choice_5 = input("\nSi vous souhaitez poursuivre, tapez 1, sinon, tapez Q pour quitter le programme : ")

                if user_choice_5 == "Q":
                    legit_request = True
                    print("Merci, et à bientôt")
                
                elif user_choice_5 == "1":
                    self.user_main_page(cursor, connexion)
                
                else:
                    print("Entrée non valide")
        
        else:
            print("Entrée non valide.")
            self.user_main_page(cursor, connexion)
    

    def products_by_category (self, user_choice, cursor, connexion):

        clear()
        id_products_returned = []
        
        query = ("SELECT id_product, product_name FROM product INNER JOIN category ON product.product_group = category.category_name WHERE category.id_category = %s")
        answer = (int(user_choice), )
        cursor.execute(query, answer)
        myresult = cursor.fetchall()

        for product in myresult:
            id_products_returned.append(product[0])
            print(product)
        
        user_choice_2 = input("\nVeuillez choisir un produit parmi ceux proposés, en entrant son numéro. Sinon, quittez le programme avec Q : ")

        if str(user_choice_2) == "Q":
            print("Merci, et à bientôt")
        
        elif int(user_choice_2) in id_products_returned:
            query = ("SELECT nutriscore FROM product WHERE product.id_product = %s")
            answer = (int(user_choice_2), )
            cursor.execute(query, answer)
            myresult = cursor.fetchall()
            
            for result in myresult:
                nutriscore_product = result[0]
            
            self.substitute_proposal(user_choice, nutriscore_product, cursor, connexion)    
        
        else:
            print("Entrée non valide.")
            self.products_by_category(user_choice, cursor, connexion)
        
    
    def substitute_proposal (self, user_choice, nutriscore_product, cursor, connexion):

        clear()
        id_products_returned = []

        if nutriscore_product == None:
            print("\nLe produit que vous avez sélectionné ne possède pas d'information liée à son nutriscore. Par défaut, nous vous proposons les produits de sa catégorie pour lesquels aucune information de nutriscore existe :\n")
            query = ("SELECT id_product, product_name, stores, url FROM product INNER JOIN category ON product.product_group = category.category_name WHERE category.id_category = %s AND product.nutriscore IS NULL")
            answer = (int(user_choice), )

        else:
            answer = (int(user_choice), nutriscore_product)
            query = ("SELECT id_product, product_name, stores, url FROM product INNER JOIN category ON product.product_group = category.category_name WHERE category.id_category = %s AND product.nutriscore <= %s")

        cursor.execute(query, answer)
        myresult = cursor.fetchall()
        
        for product in myresult:
            id_products_returned.append(product[0])
            print(product)
        
        user_choice_3 = input("\nSi vous souhaitez ajouter un produit à vos favoris, veuillez choisir entrer son numéro. Sinon, appruyez sur Q pour quitter le programme : ")

        if user_choice_3.isdigit():
            if int(user_choice_3) in id_products_returned:
                self.add_product_in_favorites(user_choice_3, cursor, connexion)
            else:
                print("\nEntrée non valide")
                self.substitute_proposal(user_choice, nutriscore_product, cursor, connexion)

        elif user_choice_3 == "Q":
            print("Merci, et à bientôt")
        
        else:
            print("\nEntrée non valide")
            self.substitute_proposal(user_choice, nutriscore_product, cursor, connexion)
        
    
    def add_product_in_favorites (self, product_id, cursor, connexion):
        
        clear()
        neutral_cursor = cursor
        legit_request = False
        
        query = ("INSERT INTO favorite (id_product) SELECT id_product FROM product WHERE product.id_product = %s")
        id_product = (int(product_id), )
        
        try:
            cursor.execute(query, id_product)
            connexion.commit()
            print("Produit ajouté aux favoris")
        except SQLcmd.Error:
            print("\nUne erreur est survenue, le produit est déjà dans vos favoris")
            pass

        while legit_request == False:
            user_choice_4 = input("\nSi vous souhaitez poursuivre, tapez 1, sinon, tapez Q pour quitter le programme : ")
            if user_choice_4 == '1':
                self.user_main_page(neutral_cursor, connexion)
                legit_request = True
            
            elif user_choice_4 == "Q":
                print("Merci, et à bientôt")
                legit_request = True
            
            else:
                print("Entrée non valide")
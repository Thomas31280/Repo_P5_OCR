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
# Connexion to server :
cnx = SQLcmd.connect(user='root', password='edgard31280', host='localhost')
cnx.close()

# Database creation

# First test on database (table creation) with connector :

dictionary = {
    "page_count": 500,
    "products": [
        {
            "categories": "Boissons,Eaux,Eaux de sources",
            "generic_name": "Eau de source naturelle",
            "product_name": "Eau De Source",
            "url": "https://fr.openfoodfacts.org/produit/3274080005003/eau-de-source-cristaline",
            "pnns_groups_1": "Beverages",
            "nutriscore_grade": "a",
            "stores": "Carrefour,Leclerc,Auchan"
        },
        {
            "stores": "Bi1,Magasins U,Carrefour,Franprix,Auchan",
            "url": "https://fr.openfoodfacts.org/produit/3017620422003/nutella-ferrero",
            "pnns_groups_1": "Sugary snacks",
            "nutriscore_grade": "e",
            "categories": "Produits à tartiner,Petit-déjeuners,Aides culinaires,Produits à tartiner sucrés,Aides à la pâtisserie,Pâtes à tartiner,Pâtes à tartiner aux noisettes,Pâtes à tartiner au chocolat,Pâtes à tartiner aux noisettes et au cacao,Aide culinaire sucrée",
            "product_name": "Nutella",
            "generic_name": "Pâte à tartiner aux noisettes et au cacao"
        }]}

#print(dictionary["products"][0])

for product in dictionary["products"]:
    for fields in product:
        print(product[fields])

print("Ceci est un {} qui va peut-être {}".format("test", "fonctionner"))
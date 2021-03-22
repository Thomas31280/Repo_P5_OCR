TABLES = {}
TABLES['product'] = (
    "CREATE TABLE `product` ("
    "  `id_product` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `url` TEXT,"
    "  `product_group` VARCHAR(60),"
    "  `nutriscore` CHAR(1),"
    "  `categories` TEXT,"
    "  `product_name` VARCHAR(150),"
    "  `generic_name` VARCHAR(200),"
    "  PRIMARY KEY (`id_product`)"
    ") ENGINE=InnoDB")

TABLES['categories'] = (
    "CREATE TABLE `categories` ("
    "  `id_category` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `category_name` VARCHAR(70),"
    "  PRIMARY KEY (`id_category`)"
    ") ENGINE=InnoDB")
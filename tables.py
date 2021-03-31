TABLES = {}

TABLES['category'] = (
    "CREATE TABLE `category` ("
    "  `id_category` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `category_name` VARCHAR(40),"
    "  PRIMARY KEY (`id_category`),"
    "  INDEX ind_category (`category_name`)"
    ") ENGINE=InnoDB")
    
TABLES['product'] = (
    "CREATE TABLE `product` ("
    "  `id_product` INT UNSIGNED NOT NULL AUTO_INCREMENT,"
    "  `url` TEXT,"
    "  `product_group` VARCHAR(60),"
    "  `categories` VARCHAR(60),"
    "  `product_name` VARCHAR(150),"
    "  `nutriscore` CHAR(1),"
    "  `stores` VARCHAR(30),"
    "  PRIMARY KEY (`id_product`),"
    "  CONSTRAINT fk_categories_category_name FOREIGN KEY (`categories`) REFERENCES category(`category_name`)"
    ") ENGINE=InnoDB")

TABLES['favorites'] = (
    "CREATE TABLE `favorites` ("
    "  `id_product` INT UNSIGNED NOT NULL UNIQUE,"
    "  `url` TEXT,"
    "  `categories` VARCHAR(60),"
    "  `product_name` VARCHAR(150),"
    "  PRIMARY KEY (`id_product`)"
    ") ENGINE=InnoDB")
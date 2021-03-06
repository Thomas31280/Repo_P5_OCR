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
    "  `categories` TEXT,"
    "  `product_name` TEXT,"
    "  `nutriscore` CHAR(1),"
    "  `stores` VARCHAR(30),"
    "  PRIMARY KEY (`id_product`),"
    "  CONSTRAINT fk_categories_category_name FOREIGN KEY (`product_group`)"
    "  REFERENCES category(`category_name`)"
    ") ENGINE=InnoDB")

TABLES['favorite'] = (
    "CREATE TABLE `favorite` ("
    "  `id_product` INT UNSIGNED NOT NULL,"
    "  PRIMARY KEY (`id_product`),"
    "  CONSTRAINT fk_id_product FOREIGN KEY (`id_product`)"
    "  REFERENCES product(`id_product`)"
    ") ENGINE=InnoDB")

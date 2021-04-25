ATTENTION : Ce programme utilise l'API OpenFoodFact. Son utilisation ( ou du moins l'initialisation du programme ) requiert donc une connexion à internet.

1 - Initialisez un dépot local sur votre machine. Vous pouvez utiliser GitBash et initialiser un repo pointant vers le dépot GitHub https://github.com/Thomas31280/Repo_P5_OCR

2 - Faites un pull du programme sur votre dépot local.

3 - Initialisez un environnement virtuel avec virtualenv sur votre machine, dans lequel vous installerez python3.

4 - Dans cet environnement virtuel, installez les librairies requises par le programme, qui figurent dans le requirement.txt. Vous pouvez les installer avec pip.

5 - Ce programme utilise des bases de données et utilise SQL. Vous devrez donc installer MySQL sur votre machine, et le configurer. Lien de téléchargement : https://dev.mysql.com/downloads/mysql/#downloads

6 - Dans votre dépot local, à la racine, vous trouverez un fichier constant_storage.py. Vous devrez l'ouvrir, et compléter la variable USER, HOST et PASSWORD avec les valeurs que vous avez choisies lors de votre installation de MySQL.

7 - Dans votre console, exécutez database_initialization.py, qui se trouve à la racine de votre dépot local. Assurez vous d'utiliser votre environnement virtuel et de vous trouver à la racine du dépot ( vérifiez votre chemin d'accès ).

8 - Votre base de données et vos tables sont désormais créées, remplies et sont opérationnelles. Vous pouvez donc exécuter le fichier user_launcher.py, et suivre les instructions qui s'affichent dans la console.
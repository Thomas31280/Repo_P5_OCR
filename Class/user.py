class User:

    def __init__(self):

        self.name = None
        self.adress = None
        self.mail = None
        self.gender = None

    def create_account(self):

        self.name = input("Veuillez indiquer votre nom")
        self.adress = input("Veuillez indiquer votre adresse")
        self.mail = input("Veuillez indiquer votre adresse e-mail")
        self.gender = input("Veuillez indiquer votre genre (M pour masculin et F pour féminin")
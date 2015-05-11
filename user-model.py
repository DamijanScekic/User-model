class User():
    ime = "ime"
    priimek = "priimek"
    email = "email"
    nalov = "naslov"

    def __init__(self, ime_user, priimek_user, email_user, naslov_user):
        self.ime = ime_user
        self.priimek = priimek_user
        self.email = email_user
        self.naslov = naslov_user

luka = User(ime_user="luka", priimek_user="Novak", email_user="luka@gmail", naslov_user="dunajska50")
miha = User(ime_user="miha", priimek_user="Pric", email_user="luka@gmail", naslov_user="dunajska50")
Anze = User(ime_user="Anze", priimek_user="Misic", email_user="luka@gmail", naslov_user="dunajska50")

#luka.ime = "Luka"
#luka.priimek = "Novak"
#luka.email = "luka@gmail"
#luka.naslov = "dunajska 50"



print luka.ime
print miha.priimek
print Anze.email


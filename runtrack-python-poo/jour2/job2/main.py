class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages

    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    def get_auteur(self):
        return self.__auteur

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def get_nb_pages(self):
        return self.__nb_pages

    def set_nb_pages(self, nb_pages):
        if isinstance(nb_pages, int) and nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être un entier positif.")

livre1 = Livre("Shining", "Stephen King", 447)
livre2 = Livre("Lovecraft Country", "Joe Hill", 384)

print(f"Livre 1 : {livre1.get_titre()} de {livre1.get_auteur()}, {livre1.get_nb_pages()} pages.")
print(f"Livre 2 : {livre2.get_titre()} de {livre2.get_auteur()}, {livre2.get_nb_pages()} pages.")

livre1.set_titre("Doctor Sleep")
livre1.set_nb_pages(531)
livre2.set_auteur("Matt Ruff")


print(f"Livre 1 : {livre1.get_titre()} de {livre1.get_auteur()}, {livre1.get_nb_pages()} pages.")
print(f"Livre 2 : {livre2.get_titre()} de {livre2.get_auteur()}, {livre2.get_nb_pages()} pages.")
 

  
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def dessiner(self):
        for i in range(self.__largeur):
            for j in range(self.__longueur):
                if i == 0 or i == self.__largeur - 1 or j == 0 or j == self.__longueur - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print("")

rectangle = Rectangle(20, 10)


print(f"Longueur : {rectangle.get_longueur()}")  
print(f"Largeur : {rectangle.get_largeur()}")    


rectangle.dessiner()


rectangle.set_longueur(16)
rectangle.set_largeur(12)

# Affichage des valeurs modifiées
print(f"Longueur : {rectangle.get_longueur()}")  
print(f"Largeur : {rectangle.get_largeur()}")    


rectangle.dessiner()
class Operation():
    def __init__(self, nbr1, nbr2):
        self.nombre1 = nbr1
        self.nombre2 = nbr2
    def addition(self):
        somme = self.nombre1 + self.nombre2
        print(somme)

initialisation = Operation(4, 6)
initialisation.addition()
dfg = Operation(78, 90)
dfg.addition()
class Instancia:
    par_classe = 2

    def __init__(self, n):
        self.par_classe = n




instancia = Instancia(4)

print(Instancia.par_classe)
print(instancia.par_classe)
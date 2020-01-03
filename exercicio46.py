class American:

    @staticmethod
    def printNationality(nacionalidade):
        print(f"A nacionalidade é {nacionalidade}")




class NewYorker(American):

    @staticmethod
    def printMinhaCidade():
        print("Eu sou de New York")


NewYorker.printNationality("Americana")
NewYorker.printMinhaCidade()
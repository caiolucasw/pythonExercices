#exercicio51 '''Write a function to compute 5/0 and use try/except to catch the exceptions.'''



try:
    resultado = 5/0

except ZeroDivisionError:
    print("Não é possível dividir por zero")



#exercicio52 Define a custom exception class which takes a string message as attribute.

class Excecoes(Exception):

    def __init__(self, mensagem):
        self.mensagem = mensagem


    def imprime(self):
        print(self.mensagem)


a = Excecoes("Erro!!")


'''Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.'''

class Itera:


    def __init__(self, n):
        self.n = n
        self.atual = 0


    def generator(self):
        for i in range(self.n):
            if i % 7 == 0:
                yield i



def main():

    iterador = Itera(22)

    for i in iterador.generator():
        print(i)

main()
'''Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).

Example: If the following n is given as input to the program:

5
Then, the output of the program should be:

500'''


def funcao(n):
    if n == 0:
        return 0

    return funcao(n-1) + 100


print(funcao(5))


lista = []
# fibonacci Squence

def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1





print(fibonacci(7))
print(lista)
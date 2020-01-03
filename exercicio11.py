'''Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether
they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010'''

valores = input("Digite números binários de 4 bits separados por virgulas: ")
lista = valores.split(',')
listaInteiros = []
listaResultante = []

for item in lista:
    listaInteiros.append(item)

for item in listaInteiros:
    num = int(item, 2)
    if num%5 == 0:
        listaResultante.append(item)

print(','.join(listaResultante))

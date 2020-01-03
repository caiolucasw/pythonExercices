'''Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number'''


# dict comprehension


numero = int(input('Digite um número: '))

dicionario = {i: i*i for i in range(1,numero+1)}

print(dicionario)
'''Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a
tuple which contains every number.
'''


csv = input('Entre com os numeros no formato csv (comma separated values): ')

lista = list(csv.split(sep=','))
tupla = tuple(csv.split(sep=','))


print(lista)
print(tupla)
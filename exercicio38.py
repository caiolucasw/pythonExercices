'''With a given tuple (1,2,3,4,5,6,7,8,9,10),
 write a program to print the first half values in one line and the last half values in one line.'''


valores = input('Digite os valores separados por virgulas: CSV ')
tupla = tuple(valores.split(','))


primeira_tupla = tupla[:int(len(tupla)/2)]
segunda_tupla =  tupla[int(len(tupla)/2):]

print(','.join(primeira_tupla))
print(','.join(segunda_tupla))

lista = []

for item in tupla:

    if int(item) %2 == 0:
        lista.append(item)

lista = tuple(lista)

print(lista)
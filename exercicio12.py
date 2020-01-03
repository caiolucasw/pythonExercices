'''Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.'''

listaFinal = []

for i in range(1000, 3001):
    texto = str(i)

    cont = 0
    for i in texto:
        if int(i)%2 == 0:
            cont += 1

    if cont == len(texto):
        listaFinal.append(texto)


print(','.join(listaFinal))



'''Please write assert statements to verify that every number in the list [2,4,6,8] is even.'''


def even(n):
    cont = 0

    lista = list(n)
    for i in lista:
        if i%2 == 0:
            cont += 1


    assert cont == len(lista), 'Lista não contém todos os elementos pares!'
    return 'Todos Pares!'


valores = [2,4,6,9]

print(even(valores))
'''Please write a binary search function which searches an item in a sorted list.
The function should return the index of element to be searched in the list.'''


def binary_search(valores, valor, ini, final):


    if ini > final or ini < 0:
        return -1

    posicao = int((ini+final)/2)

    if valores[posicao] == valor:
        return posicao

    if valor < valores[posicao]:
         return binary_search(valores, valor, ini, posicao-1)
    elif valor > valores[posicao]:
         return binary_search(valores, valor, posicao+1, final)



def procura_valor(n, valor):

    lista = list(n)

    posicao = binary_search(lista, valor, 0, len(lista) - 1)
    return posicao


li=[1,5,8,10,12,13,55,66,73,78,82,85,88,99]

print(procura_valor(li,82))


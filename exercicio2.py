def fatorial(numeros):

    fatoriais = []
    num = 1

    lista = converteInteiro(numeros)


    for i in lista:
        for numero in range(1,i+1):
             num *= numero

        fatoriais.append(str(num))

        num = 1


    print(','.join(fatoriais))


def converteInteiro(lista):

    listaInt = []

    for item in lista:
        listaInt.append(int(item))


    return listaInt


valor = input("Números para calcular o fatorial ")
lista = valor.split(' ')
fatorial(lista)


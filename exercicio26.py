def soma(a,b):
    return a+b


numeros = input('Digite dois números: FORMATO CSV ')
numeros = numeros.split(',')

print(soma(int(numeros[0]), int(numeros[1])))
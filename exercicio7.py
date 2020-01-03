'''Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''


valores = input('Digite as dimensões do vetor: ')

lista = valores.split(",")

X = int(lista[0])
Y = int(lista[1])


lista = []

array = []

# 1 jeito
resultado = [[i*j for i in range(Y)] for j in range(X)]

#2 jeito


for i in range(X):
    lista = []
    for j in range(Y):
        lista.append(j*i)

    array.append(lista)
    del(lista)


print(resultado)
print(array)





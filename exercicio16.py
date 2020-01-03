'''Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,3,5,7,9'''



string = input("Digite uma lista com números inteiros: ")
lista = string.split(',')
print(lista)
listaSquare = [str(int(i)*int(i)) for i in lista if int(i)%2 != 0]

print(','.join(listaSquare))
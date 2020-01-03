'''Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world'''


palavras = input("Digite as palavras separadas por espaços: ")

lista = palavras.split(" ")

listaResultante = []

for item in lista:
    if not item in listaResultante:
        listaResultante.append(item)


listaResultante.sort()

for item in listaResultante:
    print(item, end=" ")

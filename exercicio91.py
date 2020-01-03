import itertools

#ex91 Please write a program which accepts a string from console and print it in reverse order.

'''Example: If the following string is given as input to the program:*

rise to vote sir
Then, the output of the program should be:

ris etov ot esir'''


frase = input("Digite uma frase: ")
frase = frase[::-1]

print(frase)
# ----------------------------------------------------------------------------------------------------------------------------
#ex92 Please write a program which accepts a string from console and print the characters that have even indexes.

'''Example: If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:

Helloworld'''

lista = []
frase = input('Digite a frase: ')

for i in range(len(frase)):
    if i%2 == 0:
        lista.append(frase[i])

print(''.join(lista))

# ----------------------------------------------------------------------------------------------------------------------------
# ex93 Please write a program which prints all permutations of [1,2,3]

print(list(itertools.permutations([1,2,3])))

# ----------------------------------------------------------------------------------------------------------------------------

#ex95 - Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

'''If the following string is given as input to the program:

5
2 3 6 6 5
Then, the output of the program should be:

5'''


frase = input("Digite a sua frase: Para sair digite a letra S: ")

max = -1
runnerup = -2

while True:
    if frase in 'Ss':
        break

    for i in frase:
        if i.isdecimal():
            if int(i) > max:
                runnerup = max
                max = int(i)
            if runnerup < int(i) < max:
                runnerup = int(i)

    frase = input()

print(runnerup)
'''Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500'''

dicionario = {"D": 0, "W": 0}

valores = input("Digite o tipo de transação e a quantidade em dinheiro. Ex: D 100. Para sair digite: S ")

while True:


    if valores in 'Ss':
        break

    valores = valores.split(' ')

    if 'D' == valores[0]:
        dicionario['D'] += int(valores[1])

    elif 'W' == valores[0]:
        dicionario['W'] += int(valores[1])

    valores = input()



print(f'O resultado final dessas operações resultou em {dicionario["D"] - dicionario["W"]}R$')





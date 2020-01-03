'''Define a function which can print a dictionary where the keys are numbers between 1 and 20
(both included) and the values are square of keys.'''


dicionario = {i: i**2 for i in range(1,21)}

print(dicionario)

#exercicio32

for i in dicionario.keys():
    print(i)
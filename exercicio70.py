#Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

#ex70

import random

print(random.choice( [i for i in range(0,11) if i%2 == 0]))


#ex71 Please write a program to output a random number, which is divisible by 5 and 7,
# between 10 and 150 inclusive using random module and list comprehension.


print(random.choice([i for i in range(10,151) if i%5 == 0 and i%7==0]))

#ex72

#Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

lista1 = [i for i in range(100,201)]
lista2 = []

for i in range(5):
    lista2.append(random.choice(lista1))

print(lista2)

print(random.sample(lista2, 5))


#ex73 Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.


lista5 = random.sample([i for i in range(100,201) if i%2 == 0 ], 5)
print(lista5)

#ex74 Question
# Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.


lista6 = random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5)
print(lista6)

# ex75 Please write a program to randomly print a integer number between 7 and 15 inclusive.

print(random.randrange(7,15))


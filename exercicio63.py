'''Please write a program using generator to print the even numbers between 0 and n in comma separated
form while n is input by console.

Example: If the following n is given as input to the program:

10
Then, the output of the program should be:

0,2,4,6,8,10'''

lista=[]

def even_numbers(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i


for item in even_numbers(20):
    lista.append(str(item))

print(','.join(lista))


#exercício 64

'''Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example: If the following n is given as input to the program:

100
Then, the output of the program should be:

0,35,70'''

lista2 = []

def divisible(n):

    i = 0   

    while i < n+1:
        if i% 5 == 0 and i%7 == 0:
            yield i

        i += 1


for item in divisible(100):
    lista2.append(str(item))


print(','.join(lista2))



#ex80 Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

lista = [5,6,77,45,22,12,24]

lista_odd = [i for i in lista if i%2 != 0]
print(lista_odd)

#ex81 By using list comprehension,
# please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


lista2 = [12,24,35,70,88,120,155]
lista_divisible = [i for i in lista2 if (i%5 != 0 and i%7 != 0)]
print(lista_divisible)

#ex82 By using list comprehension, please write a program to
# print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].


lista4 = [lista2[i] for i in range(len(lista2)) if i %2 != 0]
print(lista4)


#ex83 By using list comprehension,
# please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

lista5 = [lista2[i] for i in range(0,len(lista2)) if not 2 <= i <= 4 ]
print(lista5)


#ex84 By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.


lista6 = [[[0 for k in range(8)]for j in range(5)] for i in range(3)]
print(lista6)

#ex85 By using list comprehension, please write a program to print the list after removing
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

lista7 = [lista2[i] for i in range(len(lista2)) if i !=0 and i !=4 and i!=5]
print(lista7)


#ex86 By using list comprehension, please write a program to print the
# list after removing the value 24 in [12,24,35,24,88,120,155].

lista8 = [i for i in lista2 if i != 24]
print(lista8)

#ex87 With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the above given lists.

lista9 = [1,3,6,78,35,55]

lista9 = set(lista9)
lista10 = set(lista2)


lista11 = list(set.intersection(lista9,lista10))

print(lista11)



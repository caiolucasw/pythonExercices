'''Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9'''


sentenca = input("Digite uma sentença: ")
upper = 0
lower = 0

for letra in sentenca:
    if letra.isalpha():
        if letra.isupper():
            upper += 1
        else:
            lower += 1

print(f'UPPER CASE {upper}')
print(f'LOWER CASE {lower}')
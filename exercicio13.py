'''Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''


sentenca = input("Escreva uma sentença: ")

letters = 0
digits = 0

for letra in sentenca:
    if letra.isdigit():
        digits += 1
    if letra.isalpha():
        letters += 1

print(f'LETTERS {letters}')
print(f'DIGITS {digits}')
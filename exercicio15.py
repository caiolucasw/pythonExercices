'''Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106'''

formula = "a+aa+aaa+aaaa"

digito = int(input("Forneça um dígito: "))

formula = formula.replace('a', str(digito))
formula = formula.split("+")

total = 0

for item in formula:
    total += int(item)


print(f'O resultado é: {total}')


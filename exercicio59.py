


digito = int(input("Digite um número inteiro maior que zero: "))

soma = 0

if digito > 0:

    for i in range(1,digito+1):
        soma += i/(i+1)

print(round(soma,2))

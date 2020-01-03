'''Question 21
Level 3

A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''

from math import sqrt, pow

movimentos = {'UP': 0, 'DOWN': 0, 'LEFT': 0, 'RIGHT': 0}

print("Digite os movimentos do robô no formato: MOVIMENTO PASSOS. Digite S para sair")

while True:
    movimento = input()

    if movimento in 'Ss':
        break

    movimento = movimento.split(' ')

    if movimento[0].upper() == 'UP':
        movimentos['UP'] += int(movimento[1])

    if movimento[0].upper() == 'DOWN':
        movimentos['DOWN'] += int(movimento[1])

    if movimento[0].upper() == 'RIGHT':
        movimentos['RIGHT'] += int(movimento[1])

    if movimento[0].upper() == 'LEFT':
        movimentos['LEFT'] += int(movimento[1])




#vertical

vertical = movimentos['UP'] - movimentos['DOWN']

#horizontal

horizontal = movimentos['RIGHT'] - movimentos['LEFT']

formula = sqrt(pow(vertical,2) + pow(horizontal,2))

resultado_final = round(formula)

print(resultado_final)

import random

def rollDice(number):
    dice = [0] * 6
    for i in range(number):
        x = random.randint(1,6)
        dice[x-1] = dice[x-1] + 1
    return dice

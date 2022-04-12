import random as r
import array as a

dice = a.array('i', [0,0,0,0,0,0])
rolledtimes = 0
def roll():
    rand = r.randrange(1,7)
    return rand
for i in range(1,5001):
    number = roll()
    dice.append(number)
    rolledtimes+=1
count = [dice.count(1),dice.count(2),dice.count(3),dice.count(4),dice.count(5),dice.count(6)]
for i in range(0,6):
    print('The probability is : ')
    per = str("{:.2f}".format((count[i] / 5000)*100)) + '%'
    print(i + 1, '>>', per)

import random
def rollDice(number):

    dice=[0]*6
    for i in range(number):
        random_number = random.randrange(1,7)
        dice[random_number-1]+=1
        

    for i in range(6):
        return "The probability of {} = {:.2f}%".format(i+1,(dice[i]/number)*100)

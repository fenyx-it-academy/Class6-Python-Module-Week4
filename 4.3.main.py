import my_dice

num = int(input("Enter repetition number: "))

percentages = my_dice.rollDice(num)

for i in range(6):
    per = percentages[i]/num * 100
    print("The probability of {} is {:.2f}".format(i+1, per))


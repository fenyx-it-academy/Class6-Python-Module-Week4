#Dice Percentage
#Create an array with 6 elements named dice. Fill this array with the value zero. 
# Generate a random number with a value between 1 and 6 (just like a dice) in a repetition 5000 times.
# If the value is 1, increase the element 0 in the array by 1, 
# the same applies to the values 2, 3, 4, 5 and 6. 
# The dice[0] element indicates the number of times value 1 has occurred. 
# Or in general: dice[x-1] indicates the number of times that x has been thrown.
# At the end of the repetition, print the contents of the array as percentages with 2 decimal places. 
# For example; "Percentage of throws of value 3 = 16.28%"
import random
dice = [0,0,0,0,0,0]
r = int(input('Please Enter the Number of Repetition :'))

def percentage(part, whole):
    Percentage = 100 * float(part)/float(whole)
    return str(Percentage) +' %'

def dice_percentage():
    x = [random.randint(1,6) for x in range(r)]
    for i in x:
        if i ==1:
            dice[0]+=1
        elif i ==2:
            dice[1]+=1
        elif i ==3:
            dice[2]+=1
        elif i ==4:
            dice[3]+=1
        elif i ==5:
            dice[4]+=1
        elif i ==6:
            dice[5]+=1
def dice_print():
    print('Percentage of throws of value 1 =',percentage(dice[0], r))
    print('Percentage of throws of value 2 =',percentage(dice[1], r))
    print('Percentage of throws of value 3 =',percentage(dice[2], r))
    print('Percentage of throws of value 4 =',percentage(dice[3], r))
    print('Percentage of throws of value 5 =',percentage(dice[4], r))
    print('Percentage of throws of value 6 =',percentage(dice[5], r))

dice_percentage()
print(dice)
dice_print()


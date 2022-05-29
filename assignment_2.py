import random
# II. 
# Create an array with 6 elements named dice. Fill this array with the value zero.
# Generate a random number with a value between 1 and 6 (just like a dice) in a repetition 5000 times.
# If the value is 1, increase the element 0 in the array by 1, the same applies to the values 2, 3, 4, 5 and 6.
# The dice[0] element indicates the number of times value 1 has occurred.
# Or in general: dice[x-1] indicates the number of times that x has been thrown
# At the end of the repetition, print the contents of the array as percentages with 2 decimal places. For example;
# "Percentage of throws of value 3 = 16.28%"



# dice=[0]*6

# for i in range(5000):
#     random_number = random.randrange(1,7)
#     dice[random_number-1]+=1

# for i in range(6):
#     print("Percentage of throws of value {} = {:.2f}%".format(i+1,(dice[i]/5000)*100))


print(range(6))
#As a user, I want to use a program which can calculate the greatest common divisor (GCD) of my inputs.
# Acceptance Criteria:
# Ask user the enter the number of inputs (n).
# Ask user to enter n input numbers one by one.
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# Calculate the greatest common divisor (GCD) of n numbers.
# Use gcd function in module of math.
from math import gcd
A = []
n = int(input('Please Enter the Number of Inputs :'))
i = 1
while i<=n:
    try:
        num = int(input('Please Enter the Number:'))
        A.append(num)
        i+=1
    except:
        print('Please Enter a Numeric Input :')
        i=i
print(A)
print('Greatest Common Divisor of numbers',A,'is',gcd(*A))
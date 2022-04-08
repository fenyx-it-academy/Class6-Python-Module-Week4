## 4. The Greatest Common Divisor
# As a user, I want to use a program which can calculate the `greatest common divisor (GCD)` 
# of my inputs. 

# Acceptance Criteria:
# - Ask user the enter the number of inputs (n).
# - Ask user to enter `n` input numbers one by one.
# - Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# - Calculate the greatest common divisor (GCD) of `n` numbers.
# - Use `gcd` function in module of math.
from math import gcd
import re

n = int(input("Enter a number: "))
numbers = []


for i in range(n):
    try:
        x = int(input())
        numbers.append(x)
                        
    except:
        print("Non numerical inputs.")

print(numbers)
print("gcd of the numbers: ", gcd(*numbers))

# https://github.com/alosoz/Class6-Python-Module-Week4.git
#     x = gcd(numbers[i],numbers[j])
#     print("GCD of two numbers {} and {} is: {}".format(numbers[i],numbers[i-1],x))

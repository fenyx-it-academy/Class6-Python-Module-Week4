import math
# As a user, I want to use a program which can calculate the greatest common divisor (GCD) of my inputs.

# Acceptance Criteria:

# Ask user the enter the number of inputs (n).
# Ask user to enter n input numbers one by one.
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
# Calculate the greatest common divisor (GCD) of n numbers.
# Use gcd function in module of math.
lst=[]
n = int(input("Enter the number of repetitions you want to enter: "))
for i in range(n):
    try: 
        inputs =int(input("Enter the inputs one by one: "))
        
        if n>2:
            raise SystemError

        elif inputs == 1:
            raise KeyError
            
        
        elif inputs != int(inputs):
            raise ValueError

        elif inputs<0:
            raise RecursionError
        
    except SystemError:
        print("""
        You tried to enter more than 2 inputs!!!
        Please try to enter less n!
        """)
    except KeyError:
        print("Input you entered must be bigger than 1!!!")
        

    except ValueError:
        print("input you entered is not an integer!!!")

    except RecursionError:
        print("Opps! Input you entered is negative!!!")
        

    else:
        lst.append(inputs)

    finally:
        print("Next one!")

result = math.gcd(lst[0],lst[1])

if result == 1:
    print("""    GCD can not be 1
    Please give the new values!
    """)
    
else:
    print("The greatest common divisor of",lst[0],"and",lst[1],"is",result)
    
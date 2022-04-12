import math

input_num = int(input("Please enter the number of inputs: "))

gcd = int(input())

for i in range(input_num-1):
    try:
        num = int(input())
    except:
        print("invalid input")
    else:
        gcd = math.gcd(gcd, num)
        
print("greatest common divisor", gcd)



# I.
# Write a Python program to check the validity of a password (input from users)
# Rules :
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# If password is not valid throw ValueError with a proper error message for each rule.
# If the password is valid print a success message. Use some from raise, except, assert, else and finally keywords.

import re
import time

while True:
    
    try:
        your_password=input("Enter your password: ")
        
        if not re.search("[a-z]", your_password):
            raise ValueError
        
        elif not re.search("[A-Z]", your_password):
            raise ValueError
       
        elif not re.search("[0-9]", your_password):
            raise ValueError
        
        elif not re.search("[$#@]", your_password):
            raise ValueError
        
        elif len(your_password)<6:
            raise ValueError
        
        elif len(your_password)>16:
            raise ValueError
        
    except ValueError:
        time.sleep(1.0)
        print("""Please check your password again. 
        At least one password contains: 
        one lowercase, one uppercase, one number
        one character($#@)
        min 6 digits max 16 digits!!!""")
        
    
    else:
        print("Your password is valid!!!")
        
    finally:
        print("""Executing Finally...""")
        break
     


    


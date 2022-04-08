# 1. Password
# Write a Python program to check the validity of a password (input from users)
    
# **Rules :**
# - At least 1 letter between [a-z] and 1 letter between [A-Z]
# - At least 1 number between [0-9].
# - At least 1 character from [$#@].
# - Minimum length 6 characters.
# - Maximum length 16 characters.

# If password is not valid throw `ValueError` with a proper error message for each rule. 
# If the password is valid print a success message. Use some from  `raise`, `except`, `assert`, 
# `else` and `finally` keywords.

# import re

# def check_password(password):
#     try:
        
#         if re.match('[^a-zA-Z0-9]', password):
#             raise 
#         if re.match('[^@#$]',password):

#             raise TypeError ("At least 1 letter between [a-z] and 1 letter between [A-Z], 1 number between [0-9].")
        

#     except TypeError as Type:
#         print(Type)

#     # else:

#     # finally:


# input_password = input("Enter your paasword please: ")
# check_password(input_password)

import re

password = input("Enter your password: ")


try:
    while True:
        if len(password)<6 or len(password)>16:
            raise ValueError("Invalid password: Minimum length 6 characters. Maximum length 16 characters..")
            break
        elif not re.search("[a-z]",password):
            raise ValueError("Invalid password: At least 1 letter between [a-z].")
            break
        elif not re.search("[A-Z]",password):
            raise ValueError("Invalid password: At least 1 letter between [A-Z].")
            break
        elif not re.search("[0-9]",password):
            raise ValueError("Invalid password: At least 1 letter between [0-9].")
            break
        elif not re.search("[@$#]",password):
            raise ValueError("Invalid password: At least 1 letter between [@$#].")
            break
        else:
            print("Valid Password")
            False
            break
        
except ValueError as e:
    print(ValueError, e)
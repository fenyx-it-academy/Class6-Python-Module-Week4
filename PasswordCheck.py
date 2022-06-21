# Write a Python program to check the validity of a password (input from users)
# Rules :
# At least 1 letter between [a-z] and 1 letter between [A-Z]
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.
# If password is not valid throw ValueError with a proper error message for each rule. 
# If the password is valid print a success message. Use some from raise, except, assert, else 
# and finally keywords.

import re 
x = True
while x: 
    try:
        password = input('Please Enter a Password :')
        if len(password)<6 or len(password)>16:
            raise PasswoordLengthError ("Your Password Should have minimum 6,maximum 16 characters.")
        elif not re.search("[0-9]",password):
           raise DigitUseError ("Please Use At Least One Digit")
        elif not re.search("[a-z]",password):
            raise LowercaseUseError ("Please Use At Least One Lowercase Letter")
        elif not re.search("[A-Z]",password):
            raise UppercaseUseError ("Please Use At Least One Uppercase Letter")
        elif not re.search("['$','#','@']",password):
            raise SpecialcaseUseError ("Please Use At Least One of the '$','#','@' characters")
    except PasswoordLengthError as e:
        print("Invalid Entry!..",e)    
    except DigitUseError as e:
        print("Invalid Entry!..",e)
    except LowercaseUseError as e:
        print("Invalid Entry!..",e)
    except UppercaseUseError as e:
        print("Invalid Entry!..",e)
    except SpecialcaseUseError as e:
        print("Invalid Entry!..",e)
    else:
        print('Password is Valid')
    finally:
        print('Password Check Complete')    
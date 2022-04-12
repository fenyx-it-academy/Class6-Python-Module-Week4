import re
while True : 
    x = input("Write a password : ")
    try : 
        assert len(x) >6 and len(x) <16, 'Your password must be between 6 and 16'
        if not re.search("[a-z]", x):
            raise ValueError('You must use at least a letter between [a,z]')
        elif not re.search("[A-Z]", x):
            raise ValueError('You must use at least a letter between [A-Z]')  
        elif not re.search("[0-9]", x):
            raise ValueError('You must use at least a number between [0-9]') 
        elif not re.search("[#@$]", x):
            raise ValueError('You must use special character')
        
    except ValueError as V : 
        print(V)
    except AssertionError as A:
        print(A)
    else : 
        print("Successful Password.")
        break
    finally:
        print("Have a Nice Day")

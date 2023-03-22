# Data Structure: Upper and Lower case alphabet in tuple
import string

alphabet_lower = tuple(string.ascii_lowercase)
alphabet_upper = tuple(string.ascii_uppercase)

# Data Structure: Numbers in Tuple
numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Data Structure: Special Characters in tuple
special_char = ("!", "@", "#", "$", "%", "&")

# Beginning Code Functionality
user_name = input('Create a username: ')
print('You successfully registered a username.')
print(f'Welcome {user_name}!')
print('\n- Password must include ALL the following: \n- 10 characters long \n- One upper and lower case character \n- One special character \n- One number ')

# While loop check the password
while True:
    user_password = input('\nCreate a new password:  ')

    # Check Password Strength
    has_lower = False
    has_upper = False
    has_number = False
    has_special = False

    # Iter through the password to check if any of the data is true in the password
    for char in user_password:
        if char in alphabet_lower:
            has_lower = True
        elif char in alphabet_upper:
            has_upper = True
        elif char in numbers:
            has_number = True
        elif char in special_char:
            has_special = True

    # Loop through the user's request to create a password until they successfully meet all the guidelines
    if len(user_password) < 10:
        print('Password MUST be at least 10 characters long.')
    elif not has_lower:
        print('Password MUST contain at least one lowercase letter.')
    elif not has_upper:
        print('Password MUST contain at least one uppercase letter.')
    elif not has_number:
        print('Password MUST contain at least one number 0-9.')
    elif not has_special:
        print('Password MUST contain at least one special character (i.e. !, @, #, $, %, &).')
    else:
        print('You successfully created a new password!')
        break
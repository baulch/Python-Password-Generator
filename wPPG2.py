'''
Title: A strong python password generator using two simple imports and a while loop.
Author: Tom/Tybau (myself)
Date: 26/04/2024
Description: Can be used personally or a professional setting as it produces close to uncrackable passwords, which are typically guaranteed to be strong that individually set passwords.
'''
import random
import string

def password_gen():
    password = ''
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Define a string containing all uppercase letters, lowercase letters, digits, and special characters
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    while not (has_upper and has_lower and has_digit and has_special):
        password = ''.join(random.choices(all_characters, k=random.randint(6, 21)))
        
        # Check if the password contains at least one uppercase letter, one lowercase letter, one digit, and one special character
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in string.punctuation for c in password)
    
    return password

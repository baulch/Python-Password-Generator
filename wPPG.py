'''
Title: While-looped python password generator
Author: Tybau
Date: 22/04/2025
Description: While loop to generate a password between 6-20 characters long. Must include atleast 1 upper & lower case, along with a number
'''
import random
import string
def password_gen():
    password = ''
    has_upper = False
    has_lower = False
    has_digit = False
    #Define a string containaing all upper, lower and digits
    all_characters = string.ascii_letters + string.digits
    
    #Generate random lenght between 6 and 20
    password_length = random.randint(6, 20)
    
    #Generate password
    while not (has_upper and has_lower and has_digit):
        password =''.join(random.choices(all_characters, k=random.randint(6,20)))
        
        #check is password contains at least one uppercase letter, one lwoer, and one digit
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        
    return password

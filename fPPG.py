'''
Title: for-looped python password generator
Author: Tybau
Date: 22/04/2024
Criteria: 6-18 characters long, and a minimum of 1 number, along with atleast 1 upper & lower case each.
'''
import random
def password_gen():
    password = ''
    upper_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    for i in range(random.randint(2, 6)):
        password += (upper_letters[random.randint(0, 25)])
        password += (upper_letters[random.randint(0, 25)].lower())
        password += (str(random.randint(0, 9)))
        
    return(password)

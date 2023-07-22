'''
In this project we will give a random number, the computer has to guess that nnumber
'''
'''
In this project we will have a sectret number and we will make computer to guess our number!
'''

import random

def computer_guess(x):
    low = 0
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'{guess} is it high(H), low(L) or correct(C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('The guess is correct')
    
computer_guess(1000)
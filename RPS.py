'''
In this project we will play rock papper and scissors
'''

import random

def play():
    user = input('input (r) for rock,(p) for papper,(s) for scissors: ').lower()
    computer = random.choice(['r','p','s'])
    
    if computer == user:
        return 'tie'
    
    if is_won(user,computer):
        return 'You Won!'
    return 'You Lost!'
    # r > s, p > r, s > p
    

def is_won(player,opponent):
    if(player == 'r' and opponent == 's') or (player == 'p' and opponent =='r') or \
        (player == 's' and opponent == 'p'):
            return True
    

print(play())

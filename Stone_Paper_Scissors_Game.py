#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

def play_game():
    choices = ['stone', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = random.choice(choices)
    
    print(f"Computer's choice: {computer_choice}")
    print(f"Your choice: {user_choice}")
    
    if computer_choice == user_choice:
        print("It's a tie!")
    elif (computer_choice == 'stone' and user_choice == 'scissors') or \
         (computer_choice == 'paper' and user_choice == 'stone') or \
         (computer_choice == 'scissors' and user_choice == 'paper'):
        print("Computer wins!")
    else:
        print("You win!")

play_game()


# In[ ]:





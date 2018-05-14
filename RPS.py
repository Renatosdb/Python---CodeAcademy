"""
TITLE: RPS.py
UNIT: 5
AUTHOR: Renato Lima
The program should do the following:
Prompt the user to select either Rock, Paper, or Scissors
Instruct the computer to randomly select either Rock, Paper, or Scissors
Compare the user's choice and the computer's choice
Determine a winner (the user or the computer)
Inform the user who the winner is
"""

from random import randint
from time import sleep 

options = ["R", "P", "S"]

LOSS_MESSAGE = "You lost!"
WIN_MESSAGE = "You win!"

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "The computer selected: %s" % computer_choice
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WIN_MESSAGE
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WIN_MESSAGE
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WIN_MESSAGE
  elif user_choice_index > 2:
    print "Invalid option"
    
def play_RPS():
  print "Rock, Paper, or Scissors?" 
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors: ")
  user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
  
play_RPS()

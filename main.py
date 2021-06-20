#Importing all required files
from art import logo, vs
from game_data import data
from replit import clear
import random


#Creating a function to check followers
def check(A,B):
  """Check user guess on which account has more followers"""
  A_followers = A['follower_count']
  B_followers = B['follower_count']

  if A_followers>B_followers:
    return 'A'
  
  elif B_followers > A_followers:
    return 'B' 

 # Main program
def game():
  #Define variables
  score = 0
  game_on = True
  A=random.choice(data)
  
  #While loop when player answers correctly
  while game_on:
  
    B=random.choice(data)
    
    #Handling same random choice
    while A==B:
      B= random.choice(data)
      

    #Display interface
    print(logo)

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

    print(vs)

    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

    choice= input("Who has more followers? Type 'A' or 'B': ").upper()

    result = check(A,B)

    clear()
    print(logo)
    
    #Compare choice with answer and display result
    if result == choice:
      score += 1
      print(f"You're right! Current score: {score}")
      if choice =='B':
        A = B
      

    else: 
      
      print(f"You lose. Your final score is {score}.")
      game_on = False

game()

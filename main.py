from art import logo, vs
from game_data import data
from replit import clear
import random



def check(A,B):
  """Check user guess on which account has more followers"""
  A_followers = A['follower_count']
  B_followers = B['follower_count']

  if A_followers>B_followers:
    return 'A'
  
  elif B_followers > A_followers:
    return 'B' 

def game():
  
  score = 0
  game_on = True
  A=random.choice(data)
  

  while game_on:

    B=random.choice(data)

    while A==B:
      B= random.choice(data)
      


    print(logo)

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")

    print(vs)

    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

    choice= input("Who has more followers? Type 'A' or 'B': ").upper()

    result = check(A,B)

    clear()
    print(logo)

    if result == choice:
      score += 1
      print(f"You're right! Current score: {score}")
      if choice =='B':
        A = B
      

    else: 
      
      print(f"You lose. Your final score is {score}.")
      game_on = False

game()

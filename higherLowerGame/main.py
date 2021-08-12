#import the images and data

import art
from game_data import data
import random
from replit import clear

choice = True
score = 0

#Generate random choices A and B
A= random.choice(data)
B = random.choice(data)
while(A == B):
  B = random.choice(data)
print(art.logo)

#Does the calculation and comparison to check whether the user input is correct or not
def comparison (A,B,pick):
  if(A["follower_count"] > B["follower_count"]):
    if(pick == "A"):
      return True
    else: 
      return False
  else:
    if(pick == "B"):
      return True
    else:
      return False

#displays the choices
def display(A,B):
  print(f"Compare A. {A['name']}, a {A['description']}, from {A['country']}.")
  print(art.vs)
  print(f"Compare B. {B['name']}, a {B['description']}, from {B['country']}.")
  pick = input("Who has more followers? Type 'A' or 'B': ").upper()
  results = comparison (A, B, pick)
  return results

#calculates score and increments it
def score_keeping(result):
  # print(f"score: {score}")
  if(result == True):
    return score+1
  else:
    return score

#displays the outcome
def display_score(score,choice):
  clear()
  print(art.logo)
  if(choice == True):
    print(f"You're right!. Your score is: {score}")
  else:
    print(f"Sorry! That's wrong. Your final score is: {score}")

choice =True
while(len(data)!=1 and choice !=False ):
  choice = display(A,B)
  score = score_keeping(choice)
  if(choice == True):
    data.remove(A)
    A = B
    B = random.choice (data)
    # print("hello")
  else:
    choice = False
    # print("Hello")
  display_score(score,choice)
if(len(data) == 1):
  print("You've stood the test of time. We are not Worthy!!!!")
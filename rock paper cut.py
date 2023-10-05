import random

option =("rock","paper","cut")
running =True
while running is True: 

 player = None
 computer = random.choice(option)
 while player  not in option: 
  player = input("enter rock paper cut::")

 print(f"player:{player}")
 print(f"computer:{computer}")
 
 if player == computer:
  print("draw")
 elif player=="rock" and computer=="cut":
  print("you win!")
 elif player=="cut" and computer=="paper":
  print("you win")
 elif player=="paper" and computer=="rock":
  print("you win")
 else:
  print("you lose") 
if not  input("play again (y/n)").lower() =="y": 

 runnig = False

 print("thank u for playing")
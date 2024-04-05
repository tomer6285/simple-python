import os
import random
import sys

MOVES = ["rock", "paper", "scissors"]

while 0 < 1:
  os.system("clear")
  print("Do you want to play")
  play = input()
  if play == "yes":
    break
  elif play == "no":
    sys.exit("Bye!")
  else:
    pass

score = 0
while 0 < 1:
  os.system("clear")
  print("Rock, Paper, or Scissors?")
  choice = input()
  choice = choice.lower()
  cpu_choice = random.choice(MOVES)
  print("")
  print("Your move: " + choice.upper())
  print("Computer move: " + cpu_choice.upper())
  if choice == "rock":
    if cpu_choice == "rock":
      print("Tie!")
    elif cpu_choice == "paper":
      print("You Lose!")
    elif cpu_choice == "scissors":
      score += 1
      print("You Win!")
  elif choice == "paper":
    if cpu_choice == "rock":
      score += 1
      print("You Win!")
    elif cpu_choice == "paper":
      print("Tie!")
    elif cpu_choice == "scissors":
      print("You Lose!")
  elif choice == "scissors":
    if cpu_choice == "rock":
      print("You Lose!")
    elif cpu_choice == "paper":
      score += 1
      print("You Win!")
    elif cpu_choice == "scissors":
      print("Tie!")
  print("")
  print("Press enter to play again or type quit to stop playing")
  resume = input()
  resume = resume.lower()
  if resume == "quit":
    break

os.system("clear")
print("You got a score of: " + str(score))
print("Bye!")

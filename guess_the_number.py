import os
import random

c = 0
guesses = 0

number = random.randint(1, 1000)

os.system("clear")
while c < 1:
  print("Guess the number: ")
  guess = input()
  if int(guess) < number:
    guesses += 1
    print("Higher")
    print("")
  elif int(guess) > number:
    guesses += 1
    print("Lower")
    print("")
  elif int(guess) == number:
    c = 1

print("")
print("Correct! The number was " + str(number) + " and it took you " +
      str(guesses) + " guesses")

import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

number=random.randint(1,100)
guess=None
attempts=0

while guess!=number:
  try:
    guess=int(input("Enter your guess"))
    attempts+=1
    
    if guess<number:
      print("Two low! Try again.\n")
    elif guess>number:
      print("Too high! Try again.\n")
    else:
      print(f"Correct!The number was {number}.")
      print("You guessed it in {attempts} attempts!")
  except ValueError:
    print("Please enter a valid number!\n")

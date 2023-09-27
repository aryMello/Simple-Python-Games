import random

print("Let's play 'Guess the number'!")
print()

correct = int(random.randrange(10))
count = 1
print("Try to guess the number I'm thinking...")
guess = int(input("Guess: "))

answer = "no"

while answer != "yes":
  if guess == int(correct):
    print("You got it correct in ", count, " tries!")
    break
  if guess > int(correct):
    print("Too high!")
    count+= 1
    answer = input("Give up?: ")
    guess = int(input("Guess: "))
  elif guess < int(correct):
    print("Too low!")
    count+= 1
    answer = input("Give up?: ")
    guess = int(input("Guess: "))
  else:
    print("I'm not sure, try again!")
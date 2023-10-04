import os, random, time

def rollDice(sides):
  result = random.randint(1, sides)
  return result

def roll_health():
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  health = ((dice6 * dice12) / 2) + 10
  return health

def roll_strength():
  dice6 = rollDice(6)
  dice12 = rollDice(12)
  health = ((dice6 * dice12) / 2) + 12
  return health

print("⚔ Battle Time ⚔")
print()
first_name = input("Name your legend:\n")
first_type = input("Character Type (Human, Elf, Wizard, Orc):\n")
first_health = roll_health()
print("Their health is ", first_health, "hp")
firts_strength = roll_strength()
print("Their strength is ", firts_strength, "str")
print()
print("Meet their adversary")
print()

second_name = input("Name your legend:\n")
second_type = input("Character Type (Human, Elf, Wizard, Orc):\n")
second_health = roll_health()
print("Their health is ", second_health, "hp")
second_strength = roll_strength()
print("Their strength is ", second_strength, "str")

round = 1
winner = None

while True:
  time.sleep(5)
  os.system("clear")
  print("⚔ Battle Time ⚔")
  print()
  print("The battle begins!")

  firstDice = rollDice(6)
  secondDice = rollDice(6)

  difference = abs(firts_strength - second_strength) + 1

  if firstDice > secondDice:
    second_health -= difference
    if round == 1:
      print(first_name, "wins the first blow!")
    else:
      print(first_name, "wins round", round)
  elif secondDice > firstDice:
    first_health -= difference
    if round == 1:
      print(second_name, "wins the first blow!")
    else:
      print(second_name, "wins round", round)
  else:
    print("Their swords clash and they drow round", round)

  print()
  print(first_name)
  print("HEALTH:", first_health)
  print()
  print(second_name)
  print("HEALTH:", second_health)
  print()

  if first_health <= 0:
    print(first_name, "has died!")
    winner = second_name
    break
  elif second_health <= 0:
    print(second_name, "has died!")
    winner = first_name
    break
  else:
    print("And they are both standing for the next round")
    round += 1

time.sleep(5)
os.system("clear")
print("⚔ Battle Time ⚔")
print()
print(winner, "has won in", round, "rounds!")
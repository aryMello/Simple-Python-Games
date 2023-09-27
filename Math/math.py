print("Let's play a math game!")
print()
mult = int(input("Name your multiple: "))
counter = 0
for i in range(1, 11):
  answer = i * mult
  print(i, "x", mult, "?")
  guess = int(input(":"))
  if guess == answer:
    print("You got it correct!")
    counter += 1
  else:
    print("No, that is not correct!")
if counter == 10:
  print("You answered all questions right!")
else:
  print("You got", counter, "out of 10!")
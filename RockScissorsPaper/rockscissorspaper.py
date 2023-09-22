from getpass import getpass as input

print("Let's play Rock, Scissors and Paper!")
print()
print("Choose your move: R, S or P? ")

player1 = input("Player 1: ")
print()
player2 = input("Player 2: ")
print()

if player1 == "R" or player1 == "r":
    if player2 == "R" or player2 == "r":
        print("Draw!")
    elif player2 == "S" or player2 == "s":
        print("Player 1 win!")
    elif player2 == "P" or player2 == "p":
        print("Player 2 win!")
    else:
        print("Pick a vaid move!")
elif player1 == "S" or player1 == "s":
    if player2 == "S" or player2 == "s":
        print("Draw!")
    elif player2 == "R" or player2 == "r":
        print("Player 2 win!")
    elif player2 == "P" or player2 == "p":
        print("Player 1 win!")
    else:
        print("Pick a vaid move!")
elif player1 == "P" or player1 == "p":
    if player2 == "P" or player2 == "p":
        print("Draw!")
    elif player2 == "S" or player2 == "s":
        print("Player 2 win!")
    elif player2 == "P" or player2 == "p":
        print("Player 1 win!")
    else:
        print("Pick a vaid move!")
else:
    print("Pick a vaid move!")

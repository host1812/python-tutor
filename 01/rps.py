player1 = input("player1: ")
player2 = input("player2: ")

if player1 == "r" and player2 == "s":
    print("player1 wins")
elif player1 == "p" and player2 == "r":
    print ("player1 wins")
elif player1 == "s" and player2 == "p":
    print("player1 wins")
elif player1 == player2:
    print("nobody wins")
else:
    print("player2 wins")
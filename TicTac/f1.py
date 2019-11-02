from game import Game
from layout import Layout

choice = str(input("Do you want to play? (Y/N)"))
player1 = Game.play(choice)
print("You choosed {}".format(player1))

Layout.layout()
print("")

index = int(input("Enter position:"))
Layout.index(index, player1)

Layout.layout()



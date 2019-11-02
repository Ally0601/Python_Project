from layout import Layout


class Game(object):
    def __init__(self):
        pass

    @staticmethod
    def play(choice):

        if choice == "Y" or choice == 'y':
            c = input("Choose X or O")
            if c == "X" or c == "x":
                return "X"
            elif c == "O" or c == "o":
                return "O"
            else:
                print("Are you serious?")

        elif choice == "N" or choice == "n":
            print("See you around then!")
        else:
            print("Do you even understand English?")


class Layout(object):
    row1 = {1: '-', 2: '-', 3: '-'}
    row2 = {4: '-', 5: '-', 6: '-'}
    row3 = {7: '-', 8: '-', 9: '-'}

    def __init__(self):
        pass

    @staticmethod
    def layout():
        for items in Layout.row1:
            print(Layout.row1[items], end=" ")

        print()

        for items in Layout.row2:
            print(Layout.row2[items], end=" ")

        print()

        for items in Layout.row3:
            print(Layout.row3[items], end=" ")

    @staticmethod
    def index(index, player1):
        if index in range(1, 4):
            Layout.row1[index] = player1
        elif index in range(4, 7):
            Layout.row2[index] = player1
        elif index in range(7, 10):
            Layout.row3[index] = player1
        else:
            print("There are only 9 places, genius!")

    @staticmethod
    def logic():
        if row1[1], row[2]
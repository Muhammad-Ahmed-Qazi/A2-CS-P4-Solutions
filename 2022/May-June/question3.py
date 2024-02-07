# 3a
class Card:
    # PRIVATE number : INTEGER
    # PRIVATE colour : STRING

    def __init__(self, number, colour):
        self.__number = number
        self.__colour = colour

    # 3b
    def GetNumber(self):
        return self.__number

    def GetColour(self):
        return self.__colour

# 3c    
array = [None for i in range(30)]
# DECLARE player1[0:3] : ARRAY OF Card
player1 = []

try:
    with open("./2022/May-June/CardValues.txt", "r") as file:
        for i in range(30):
            number = file.readline()
            colour = file.readline()
            obj = Card(number, colour)
            array[i] = obj
except FileNotFoundError:
    print("File not found!")
except:
    print("Some other error!")

# 3d
def ChooseCard(index):
    while True:
        if index >= 1 and index <= 30:
            index -= 1
            if index not in player1:
                player1.append(index)
                return index
            else:
                print("Card has already been selected!")
        else:
            print("Index out of range (1-30)!")
        index = int(input("Enter a card:\n>>> "))

# 3e
for i in range(4):
    index = int(input("Enter a card:\n>>> "))
    ChooseCard(index)

for item in player1:
    print(f"Number: {array[item].GetNumber()}Colour: {array[item].GetColour()}")


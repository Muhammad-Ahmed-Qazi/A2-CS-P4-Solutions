# 2a
class Character():
    # PRIVATE name : STRING
    # PRIVATE xCoordinate : INTEGER
    # PRIVATE yCoordinate : INTEGER

    def __init__(self, name, x, y):
        self.__name = name
        self.__xCoordinate = x
        self.__yCoordinate = y
    
    # 2b
    def GetName(self):
        return self.__name
    
    def GetX(self):
        return self.__xCoordinate
    
    def GetY(self):
        return self.__yCoordinate
    
    # 2c
    def ChangePosition(self, xChange, yChange):
        self.__xCoordinate += xChange
        self.__yCoordinate += yChange

# 2d
# Main Program
array = [None for i in range(10)]

try:
    with open("./2022/October-November/Characters.txt", "r") as file:
        for i in range(10):
            name = file.readline().strip().lower()
            x = file.readline().strip()
            y = file.readline().strip()
            obj = Character(name, int(x), int(y))
            array[i] = obj
except FileNotFoundError:
    print("File not found!")
except:
    print("Some other error!")

# 2e
index = 0
flag = False

while True:
    name = input("Input a character's name:\n>>> ")
    for i in range(len(array)):
        if array[i].GetName() == name.lower():
            index = i
            flag = True
            break
    if flag: break

# 2f
moveChars = ['A', 'B', 'C', 'D']
while True:
    move = input("Enter move: (A, W, S or D)\n>>> ")
    if move in moveChars:
        if move == 'A': array[index].ChangePosition(-1, 0)
        elif move == 'B': array[index].ChangePosition(0, 1)
        elif move == 'C': array[index].ChangePosition(0, -1)
        elif move == 'D': array[index].ChangePosition(1, 0)
        print(f"{array[index].GetName()} has changed coordinates to X = {array[index].GetX()} and Y = {array[index].GetY()}")
        break
    else:
        print("Enter valid character! Try again!")

    
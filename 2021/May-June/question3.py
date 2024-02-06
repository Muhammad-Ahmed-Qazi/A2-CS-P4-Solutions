# 3a
class TreasureChest:
    # DECLARE question : STRING
    # DECLARE answer : INTEGER
    # DECLARE points: INTEGER

    def __init__(self, question, answer, points):
        self.__question  = question
        self.__answer = int(answer)
        self.__points = int(points)
    
    # 3c
    def getQuestion(self):
        return self.__question
    
    def checkAnswer(self, ans):
        return (ans == self.__answer)
    
    def getPoints(self, attempts):
        if attempts == 1: return self.__points
        elif attempts == 2: return (int(self.__points / 2))
        elif attempts == 3 or attempts == 4: return (int(self.__points / 4))
        else: return 0


# 3b
# DECLARE arrayTreasure[0:4] : ARRAY OF TreasureChest
arrayTreasure = []

def readData():
    global arrayTreasure

    try:
        with open("./2021/May-June/TreasureChestData.txt", "r") as file:
            for line in range(5):
                question = file.readline()
                answer = file.readline()
                points = file.readline()

                obj = TreasureChest(question, answer, points)
                arrayTreasure.append(obj)
    except:
        print("File TreasureChestData.txt was not found!")


# Main Program
readData()
whichQ = int(input("Enter a question number between 1 and 5:\n>>> "))

question = arrayTreasure[whichQ - 1]
attempts = 0

while True:
    attempts += 1
    print(question.getQuestion(), end="")
    answer = int(input("Your answer:\n>>> "))
    if question.checkAnswer(answer): break
    print("Incorrect answer! Please try again!")

print("You scored:", question.getPoints(attempts))
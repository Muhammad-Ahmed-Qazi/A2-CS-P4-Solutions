# 2a
Queue = ["" for i in range(50)] # DECLARE Queue : ARRAY[0:49] AS STRING
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global TailPointer

    if TailPointer == len(Queue) - 1:
        print("Queue is full!")
    else:
        Queue[TailPointer] = Data
        TailPointer += 1

def Dequeue():
    global HeadPointer

    if HeadPointer == TailPointer:
        print("Queue is empty!")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer]

# 2b
def ReadData():
    with open("2023/October-November/P 41/QueueData.txt", "r") as file:
        line = file.readline().strip()
        while line != "":
            Enqueue(line)
            line = file.readline().strip()

# 2c
class RecordData:
    # DECLARE ID : STRING
    # DECLARE Total : INTEGER

    def __init__(self):
        self.ID = ''
        self.Total = 0

# DECLARE Records : ARRAY[0:49] AS RecordData
Records = [RecordData() for i in range(50)]
NumberRecords = 0

def TotalData():
    global NumberRecords

    DataAccessed = Dequeue()
    Flag = False

    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        Flag = True
        NumberRecords += 1
    else:
        for X in range(0, NumberRecords):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True
    
    if Flag == False:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1

# 2d
def OutputRecords():
    for Index in range(NumberRecords):
        print(f"ID {Records[Index].ID} Total {Records[Index].Total}")

# 2e
# Main Program
ReadData()

while HeadPointer != TailPointer - 1:
    TotalData()

OutputRecords()
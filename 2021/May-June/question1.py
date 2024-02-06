# 1a
# Declaration of record type *node*
class node:
    def __init__(self):
        # DECLARE data : INTEGER
        # DECLARE nextNode : INTEGER
        self.data = 0
        self.nextNode = 0

# 1b
startPointer = 0
emptyList = 5

linkedList = [node() for i in range(10)]

linkedList[0].data = 1; linkedList[0].nextNode = 1
linkedList[1].data = 5; linkedList[1].nextNode = 4
linkedList[2].data = 6; linkedList[2].nextNode = 7
linkedList[3].data = 7; linkedList[3].nextNode = -1
linkedList[4].data = 2; linkedList[4].nextNode = 2
linkedList[5].data = 0; linkedList[5].nextNode = 6
linkedList[6].data = 0; linkedList[6].nextNode = 8
linkedList[7].data = 56; linkedList[7].nextNode = 3
linkedList[8].data = 0; linkedList[8].nextNode = 9
linkedList[9].data = 0; linkedList[9].nextNode = -1

# 1c
def outputNodes(array, sp):
    while sp != -1:
        print(array[sp].data, end=" ")
        sp = array[sp].nextNode
    print()

# 1d
def addNode(array, sp, empty):
    data = input("Enter the data to be added: \n>>> ")
    if empty != -1:
        array[empty].data = data
        while True:
            if array[sp].nextNode == -1:
                break
            sp = array[sp].nextNode
        array[sp].nextNode = empty
        # empty, array[empty].nextNode = array[empty].nextNode, -1
        temp = array[empty].nextNode
        array[empty].nextNode = -1
        empty = temp
        return True
    else:
        return False



# Main Program
outputNodes(linkedList, startPointer)

result = addNode(linkedList, startPointer, emptyList)
if not result: print("No available space! Data not added!")
else: print("Data added successfully!")

outputNodes(linkedList, startPointer)

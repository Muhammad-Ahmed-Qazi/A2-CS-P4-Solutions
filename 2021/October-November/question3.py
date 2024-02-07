# 3a
# DECLARE arrayNodes[0:19, 0:2] : ARRAY OF INTEGERS
arrayNodes = [[None, None, None] for i in range(20)]

rootPointer = -1
freeNode = 0

# 3b
def AddNode():
    global arrayNodes, rootPointer, freeNode
    
    nodeData = int(input("Enter the data:\n>>> "))
    if freeNode <= 19:
        arrayNodes[freeNode][0] = -1
        arrayNodes[freeNode][1] = nodeData
        arrayNodes[freeNode][2] = -1
        if rootPointer == -1: rootPointer = 0
        else:
            placed = False
            currentNode = rootPointer
            while not placed:
                if nodeData < arrayNodes[currentNode][1]:
                    if arrayNodes[currentNode][0] == -1:
                        arrayNodes[currentNode][0] = freeNode
                        placed = True
                    else: currentNode = arrayNodes[currentNode][0]
                else:
                    if arrayNodes[currentNode][2] == -1:
                        arrayNodes[currentNode][2] = freeNode
                        placed = True
                    else: currentNode = arrayNodes[currentNode][2]
        freeNode += 1
    else: print("Tree is full!")

# 3c
def PrintAll():
    for item in arrayNodes:
        print(f"{item[0]}\t{item[1]}\t{item[2]}")
    print()

# 3e
def InOrder(node):
    if node != -1:
        InOrder(arrayNodes[node][0])
        print(arrayNodes[node][1])
        InOrder(arrayNodes[node][2])

# 3d
# Main Program
for i in range(10):
    AddNode()

# PrintAll()
InOrder(rootPointer)
# 2a
arrayData = [0 for i in range(10)]

arrayData[0] = 10
arrayData[1] = 5
arrayData[2] = 6
arrayData[3] = 7
arrayData[4] = 1
arrayData[5] = 12
arrayData[6] = 13
arrayData[7] = 15
arrayData[8] = 21
arrayData[9] = 8

# 2b
def linearSearch(data):
    global arrayData
    
    for item in arrayData:
        if item == int(data): return True
    
    return False

# 2c
def bubbleSort():
    theArray = arrayData
    # DECLARE temp : INTEGER
    temp = 0

    for x in range(len(theArray)):
        for y in range(len(theArray) - 1):
            if theArray[y] > theArray[y + 1]:
                temp = theArray[y]
                theArray[y] = theArray[y + 1]
                theArray[y + 1] = temp
    
    return theArray


# Main Program
data = input("Enter a value to search for:\n>>> ")
result = linearSearch(data)
if not result: print("Value entered was not found!")
else: print("Value entered was found!")

print(bubbleSort())
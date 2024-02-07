import random as r

# 2a
arrayData = [[None for i in range(10)] for i in range(10)]

for i in range(10):
    for j in range(10):
        arrayData[i][j] = r.randint(1, 100)

# 2bii
def display():
    for item in arrayData:
        for element in item:
            print(element, end=" ")
        print()

print("Before:")
display()

# 2c
def binarySearch(searchArray, lower, upper, searchValue):
    if upper > lower:
        mid = int((lower + (upper - 1)) / 2)
        if searchArray[0][mid] == searchValue:
            return mid
        else:
            if searchArray[0][mid] > searchValue:
                return binarySearch(searchArray, lower, mid - 1, searchValue)
            else:
                return binarySearch(searchArray, mid + 1, upper, searchValue)
    else: return -1

# 2b
arrayLength = 10
for x in range(arrayLength):
    for y in range(arrayLength - 1):
        for z in range(arrayLength - y - 1):
            if arrayData[x][z] > arrayData[x][z + 1]:
                tempValue = arrayData[x][z]
                arrayData[x][z] = arrayData[x][z + 1]
                arrayData[x][z + 1] = tempValue

print("After:")
display()

val = input("Enter number in the first line of the array:\n>>> ")
print(f"Result:", binarySearch(arrayData, 0, arrayLength, int(val)))
val = input("Enter number not in the first line of the array:\n>>> ")
print(f"Result:", binarySearch(arrayData, 0, arrayLength, int(val)))
# 1a
animals = [None for i in range(10)]

# 1b
animals[0] = "horse"
animals[1] = "lion"
animals[2] = "rabbit"
animals[3] = "mouse"
animals[4] = "bird"
animals[5] = "deer"
animals[6] = "whale"
animals[7] = "elephant"
animals[8] = "kangaroo"
animals[9] = "tiger"

# 1c
def SortDescending():
    arrayLength = len(animals)
    temp = ""

    for x in range(0, arrayLength - 1):
        for y in range(0, arrayLength - x - 1):
            if animals[y][:1] < animals[y + 1][:1]:
                temp = animals[y]
                animals[y] = animals[y + 1]
                animals[y + 1] = temp

# 1d
# Main program
SortDescending()
for item in animals:
    print(item)
# 2a
class SaleData:
    def __init__(self):
        self.id = ""
        self.quantity = 0

# 2b
circularQueue = [SaleData() for i in range(5)]
head = 0
tail = 0
numberOfItems = 0

for item in circularQueue:
    item.id = ""
    item.quantity = -1

head = tail = numberOfItems = 0

# 2c
def Enqueue(record):
    global head, tail, numberOfItems

    if numberOfItems < len(circularQueue):
        circularQueue[tail] = record
        tail += 1
        if tail == len(circularQueue):
            tail = 0
        numberOfItems += 1
        return 1
    else:
        return -1
    
# 2d
def Dequeue():
    global head, tail, numberOfItems

    if numberOfItems != 0:
        record = circularQueue[head]
        head += 1
        numberOfItems -= 1
        return record
    else:
        return SaleData()
    
# 2e
def EnterRecord():
    itemId = input("Enter ID:\n>>> ")
    itemQuantity = int(input("Enter quantity:\n>>> "))
    record = SaleData()
    record.id = itemId
    record.quantity = itemQuantity

    result = Enqueue(record)
    if result == 1: print("Stored")
    else: print("Full")

# 2f
# Main program
for i in range(6):
    EnterRecord()

result = Dequeue()
if result.id != "":
    print("ID:", result.id)
else: print("Queue is empty.")

EnterRecord()

for item in circularQueue:
    print("Sales ID:", item.id, "\nSales quantity:", item.quantity)

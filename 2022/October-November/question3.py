# 3a
queue = [None for i in range(100)]
head = -1
tail = 0

# 3b
def Enqueue(data):
    global head, tail

    if head != tail:
        queue[tail] = data
        tail += 1
        return True
    else:
        return False

def recursiveOutput(start):
    global head
    if start == (head + 1): return queue[start]
    else:
        return recursiveOutput(start - 1) + queue[start]

# 3c
# Main Program
flag = True

for i in range(20):
    flag = Enqueue(i + 1)

if flag: print("Successful!")
else: print("Unsuccessful!")

print(recursiveOutput(19))
# 1a
stackData = [None for i in range(10)]
stackPointer = 0

# 1b
def display():
    for i in range(len(stackData)):
        print(f"{i + 1}: {stackData[i]}")
    print("Stack pointer:", stackPointer)

# 1c
def push(data):
    global stackPointer

    if stackPointer != (len(stackData)):
        stackData[stackPointer] = data
        stackPointer += 1
        return True
    else: return False

# 1e
def pop():
    global stackPointer

    if stackPointer != 0:
        stackPointer -= 1
        return stackData[stackPointer]
    else: return -1

# 1d
# Main Program
for i in range(11):
    data = input("Enter an integer:\n>>> ")
    if push(data): print("Data successfully added!")
    else: print("Stack is full! Can't add anymore!")

display()

print(f"Popped: {pop()}")
print(f"Popped: {pop()}")

display() # Pop function DOES NOT remove the value from the stack!
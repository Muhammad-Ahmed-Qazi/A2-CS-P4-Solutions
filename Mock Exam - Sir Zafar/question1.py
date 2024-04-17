# 1a
def IterativeFactorial(Number):
    if Number == 0:
        return 1
    else:
        Result = 1
        for Count in range(1, Number + 1):
            Result = Result * Count
        return Result

print("Iterative function:")
print(IterativeFactorial(5))
print(IterativeFactorial(0))
print(IterativeFactorial(3))

# 1b
def RecursiveFactorial(Number):
    if Number == 0:
        return 1
    else:
        return Number * RecursiveFactorial(Number - 1)

print("Recursive function:")
print(RecursiveFactorial(5))
print(RecursiveFactorial(0))
print(RecursiveFactorial(3))
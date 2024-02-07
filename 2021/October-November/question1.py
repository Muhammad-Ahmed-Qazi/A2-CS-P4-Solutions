# 1a
def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return (Unknown(X + 1, Y) * 2)
    else:
        if X == Y: return 1
        else:
            print(X + Y)
            return int(Unknown(X - 1, Y) / 2)

# 1c
def IterativeUnknown(X, Y):
    result = 1

    while X != Y:
        print(X + Y)
        if X < Y:
            X += 1
            result = result * 2
        else:
            X -= 1
            result = result / 2
    
    return int(result)
    


# Main Program
print(f"X = {10}, Y = {15}")
print(Unknown(10, 15))

print(f"X = {10}, Y = {10}")
print(Unknown(10, 10))

print(f"X = {15}, Y = {10}")
print(Unknown(15, 10))

# 1d
print(f"X = {10}, Y = {15}")
print(IterativeUnknown(10, 15))

print(f"X = {10}, Y = {10}")
print(IterativeUnknown(10, 10))

print(f"X = {15}, Y = {10}")
print(IterativeUnknown(15, 10))